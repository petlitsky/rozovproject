import time
import threading
import gpiod
from PySide6.QtCore import QObject, Signal


class FanController(QObject):
    fan_speed_updated = Signal(int)  # скорость в %

    def __init__(self, chip_name="gpiochip4", pin_offset=12, parent=None):
        """
        На Raspberry Pi 5 основной разъем GPIO обычно находится на gpiochip4.
        GPIO12 на разъеме = pin_offset 12.
        """
        super().__init__(parent)
        self._chip_name = chip_name
        self._pin_offset = pin_offset
        self._speed = 0  # 0-100%
        self._is_initialized = False

        self._line = None
        self._pwm_thread = None
        self._running = False

        self._init_gpio()

    def _init_gpio(self):
        try:
            # Открываем чип и запрашиваем линию
            chip = gpiod.Chip(self._chip_name)
            self._line = chip.get_line(self._pin_offset)
            self._line.request(
                consumer="FanController", type=gpiod.LINE_REQ_DIR_OUT
            )

            self._is_initialized = True
            self._running = True

            # Запускаем фоновый поток для генерации ШИМ
            self._pwm_thread = threading.Thread(
                target=self._pwm_loop, daemon=True
            )
            self._pwm_thread.start()
            print("[FAN] Успешно инициализирован через gpiod")

        except Exception as e:
            self._is_initialized = False
            print(f"[FAN] Ошибка инициализации gpiod: {e}")

    def _pwm_loop(self):
        """Фоновый цикл генерации ШИМ (период 10 мс = 100 Гц)"""
        period = 0.01  # 10 мс
        while self._running:
            if self._speed <= 0:
                self._line.set_value(0)
                time.sleep(period)
            elif self._speed >= 100:
                self._line.set_value(1)
                time.sleep(period)
            else:
                high_time = period * (self._speed / 100.0)
                low_time = period - high_time

                self._line.set_value(1)
                time.sleep(high_time)
                self._line.set_value(0)
                time.sleep(low_time)

    def set_speed(self, speed: int) -> None:
        if not self._is_initialized:
            return

        speed = max(0, min(100, speed))
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