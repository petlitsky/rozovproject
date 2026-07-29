import threading
import time
import gpiod
from PySide6.QtCore import QObject, Signal


class FanController(QObject):
    fan_speed_updated = Signal(int)  # скорость в %

    def __init__(self, pin_offset=12, parent=None):
        # Обязательно передаем parent в QObject!
        super().__init__(parent)
        chip_name = "/dev/gpiochip4"
        try:
            gpiod.Chip(chip_name).close()
        except Exception:
            chip_name = "/dev/gpiochip0"

        self._chip_name = str(chip_name)
        self._pin_offset = int(pin_offset)  # Пин должен быть строго int!
        self._speed = 0  # 0-100%
        self._is_initialized = False

        self._chip = None
        self._line = None
        self._pwm_thread = None
        self._running = False

        self._init_gpio()

    def _init_gpio(self):
        try:
            # 1. Открываем чип
            self._chip = gpiod.Chip(self._chip_name)

            # 2. Получаем линию по номеру пина (int)
            self._line = self._chip.get_line(self._pin_offset)

            # 3. Запрашиваем управление пином на выход
            self._line.request(
                consumer="FanController", type=gpiod.LINE_REQ_DIR_OUT
            )

            self._is_initialized = True
            self._running = True

            # 4. Запускаем фоновый поток ШИМ
            self._pwm_thread = threading.Thread(
                target=self._pwm_loop, daemon=True
            )
            self._pwm_thread.start()
            print(
                f"[FAN] Успешно инициализирован gpiod на пине {self._pin_offset}"
            )

        except Exception as e:
            self._is_initialized = False
            print(f"[FAN] Ошибка инициализации gpiod: {e}")

    def _pwm_loop(self):
        """Фоновый цикл ШИМ (период 10 мс = 100 Гц)"""
        period = 0.01  # 10 мс
        while self._running:
            if self._speed <= 0:
                if self._line:
                    self._line.set_value(0)
                time.sleep(period)
            elif self._speed >= 100:
                if self._line:
                    self._line.set_value(1)
                time.sleep(period)
            else:
                high_time = period * (self._speed / 100.0)
                low_time = period - high_time

                if self._line:
                    self._line.set_value(1)
                time.sleep(high_time)
                if self._line:
                    self._line.set_value(0)
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

        if self._line:
            self._line.set_value(0)
            self._line.release()

        if self._chip:
            self._chip.close()