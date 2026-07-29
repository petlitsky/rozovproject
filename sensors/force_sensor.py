import time
from PySide6.QtCore import QThread, Signal
from hx711 import HX711


class ForceSensorWorker(QThread):
    force_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=24, pd_sck_pin=25, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.scale_ratio = 420.0  # Калибровочный коэффициент
        self._running = True
        self.hx = None

    def run(self):
        try:
            print(f"[Force Sensor] Запуск HX711 (DOUT={self.dout_pin}, SCK={self.pd_sck_pin})...")
            self.hx = HX711(dout_pin=self.dout_pin, pd_sck_pin=self.pd_sck_pin)
            
            # Настройка и автоматическая тарировка
            self.hx.set_reference_unit(self.scale_ratio)
            self.hx.reset()
            self.hx.tare()

            print("[Force Sensor] HX711 успешно обнулен и готов.")

            while self._running:
                val = self.hx.get_weight(5)
                
                # Фильтр шума около нуля
                if abs(val) < 0.1:
                    val = 0.0

                self.force_updated.emit(float(val))
                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка чтения Force Sensor (HX711): {e}"
            print(f"[Force Error] {error_msg}")
            self.error_occurred.emit(error_msg)
        finally:
            self._cleanup()

    def stop(self):
        """Плавная остановка потока."""
        self._running = False
        self.wait()

    def _cleanup(self):
        if self.hx and hasattr(self.hx, "clean_up"):
            try:
                self.hx.clean_up()
            except Exception:
                pass
            print("[Force Sensor] Ресурсы GPIO освобождены.")