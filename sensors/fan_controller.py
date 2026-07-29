import os
import threading
import time
import gpiod
from PySide6.QtCore import QObject, Signal


class FanController(QObject):
    fan_speed_updated = Signal(int)  # скорость в %

    def __init__(self, parent=None, pin_offset=12):
        super().__init__(parent)

        self._pin_offset = int(pin_offset)
        self._speed = 0
        self._is_initialized = False

        self._request = None
        self._pwm_thread = None
        self._running = False

        self._init_gpio()

    def _find_chip_path(self):
        """Ищет реальный путь к gpiochip в /dev/"""
        dev_files = sorted(
            [f for f in os.listdir("/dev") if f.startswith("gpiochip")]
        )

        for dev in dev_files:
            chip_path = f"/dev/{dev}"
            try:
                # Проверяем доступность чипа в gpiod v2
                with gpiod.Chip(chip_path) as chip:
                    info = chip.get_info()
                    if self._pin_offset < info.num_lines:
                        return chip_path
            except Exception:
                continue
        return None

    def _init_gpio(self):
        try:
            chip_path = self._find_chip_path()
            if not chip_path:
                raise FileNotFoundError(
                    f"Не найден чип в /dev/, содержащий пин №{self._pin_offset}"
                )

            # --- НОВЫЙ СИНТАКСИС GPIOD v2 ---
            # Создаем конфигурацию направления (OUTPUT)
            line_cfg = {
                self._pin_offset: gpiod.LineSettings(
                    direction=gpiod.line.Direction.OUTPUT,
                    output_value=gpiod.line.Value.INACTIVE,
                )
            }

            # Запрашиваем линию у ядра
            self._request = gpiod.request_lines(
                chip_path, consumer="FanController", config=line_cfg
            )

            self._is_initialized = True
            self._running = True

            # Запускаем фоновый ШИМ-поток
            self._pwm_thread = threading.Thread(
                target=self._pwm_loop, daemon=True
            )
            self._pwm_thread.start()
            print(
                f"[FAN] Вентилятор инициализирован (gpiod v2) на {chip_path}, пин {self._pin_offset}"
            )

        except Exception as e:
            self._is_initialized = False
            print(f"[FAN] Ошибка инициализации gpiod v2: {e}")

    def _pwm_loop(self):
        """Фоновый цикл генерации ШИМ под gpiod v2"""
        period = 0.01  # 10 мс (100 Гц)
        VAL_ON = gpiod.line.Value.ACTIVE
        VAL_OFF = gpiod.line.Value.INACTIVE

        while self._running:
            if self._speed <= 0:
                if self._request:
                    self._request.set_value(self._pin_offset, VAL_OFF)
                time.sleep(period)
            elif self._speed >= 100:
                if self._request:
                    self._request.set_value(self._pin_offset, VAL_ON)
                time.sleep(period)
            else:
                high_time = period * (self._speed / 100.0)
                low_time = period - high_time

                if self._request:
                    self._request.set_value(self._pin_offset, VAL_ON)
                time.sleep(high_time)
                if self._request:
                    self._request.set_value(self._pin_offset, VAL_OFF)
                time.sleep(low_time)

    def set_speed(self, speed: int) -> None:
        if not self._is_initialized:
            return

        speed = max(0, min(100, int(speed)))
        self._speed = speed
        self.fan_speed_updated.emit(speed)

    def get_speed(self) -> int:
        return self._speed

    def stop(self):
        self.set_speed(0)

    def cleanup(self):
        self._running = False
        if self._pwm_thread and self._pwm_thread.is_alive():
            self._pwm_thread.join(timeout=0.2)

        if self._request:
            self._request.set_value(
                self._pin_offset, gpiod.line.Value.INACTIVE
            )
            self._request.release()