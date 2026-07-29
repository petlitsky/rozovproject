import time
from PySide6.QtCore import QThread, Signal
from hx711_gpiozero import HX711


class ForceSensorWorker(QThread):
    force_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=24, pd_sck_pin=25, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self._running = True
        self.hx = None

    def run(self):
        try:
            # Инициализация датчика
            self.hx = HX711(dout=self.dout_pin, sck=self.pd_sck_pin)

            # Безопасное получение начального смещения (тарировка)
            zero_offset = self.hx.value
            scale_ratio = 420.0  # Калибровочный коэффициент

            while self._running:
                raw_val = self.hx.value

                if raw_val is not None:
                    # Расчет усилия
                    force = (raw_val - zero_offset) / scale_ratio
                    self.force_updated.emit(force)
                    print(force)

                # Используем msleep вместо time.sleep для лучшей интеграции с Qt
                self.msleep(100)

        except Exception as e:
            self.error_occurred.emit(f"Ошибка чтения HX711: {e}")
        finally:
            self._cleanup()

    def stop(self):
        """Плавная остановка потока."""
        self._running = False
        self.wait()  # Ожидаем завершения run()

    def _cleanup(self):
        """Очистка ресурсов GPIO."""
        if self.hx and hasattr(self.hx, "close"):
            try:
                self.hx.close()
            except Exception:
                pass