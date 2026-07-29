import time
from PySide6.QtCore import QThread, Signal
from hx711 import HX711


class TorqueSensorWorker(QThread):
    torque_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=18, pd_sck_pin=23, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.scale_ratio = 420.0  # Калибровочный коэффициент для BTQ-403A
        self._running = True
        self.hx = None

    def run(self):
        try:
            print(f"[Torque BTQ-403A] Запуск HX711 (DOUT={self.dout_pin}, SCK={self.pd_sck_pin})...")
            self.hx = HX711(dout_pin=self.dout_pin, pd_sck_pin=self.pd_sck_pin)
            
            # Настройка и автоматическая тарировка
            self.hx.set_reference_unit(self.scale_ratio)
            self.hx.reset()
            self.hx.tare()

            print("[Torque BTQ-403A] HX711 успешно обнулен и готов.")

            while self._running:
                val = self.hx.get_weight(5)
                
                # Фильтр шума около нуля
                if abs(val) < 0.05:
                    val = 0.0

                self.torque_updated.emit(float(val))
                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка чтения Torque Sensor (HX711): {e}"
            print(f"[Torque Error] {error_msg}")
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
            print("[Torque BTQ-403A] Ресурсы GPIO освобождены.")