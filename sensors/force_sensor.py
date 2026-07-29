from PySide6.QtCore import QThread, Signal
import time
from hx711_gpiozero import HX711

class ForceSensorWorker(QThread):
    force_updated = Signal(float)
    
    # Имена параметров dout и sck (по умолчанию 24 и 23)
    def __init__(self, dout_pin=24, pd_sck_pin=23):
        super().__init__()
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self._running = True
        self.hx = None

    def run(self):
        try:
            # Передаем dout и sck вместо pd_sck
            self.hx = HX711(dout=self.dout_pin, sck=self.pd_sck_pin)
            
            # В hx711-gpiozero для чтения значения используется свойство .value
            # Потребуется тарировка (смещение):
            zero_offset = self.hx.value
            scale_ratio = 420.0  # Калибровочный коэффициент

            while self._running:
                raw_val = self.hx.value
                # Расчет усилия
                force = (raw_val - zero_offset) / scale_ratio
                self.force_updated.emit(force)
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Ошибка чтения HX711: {e}")

    def stop(self):
        self._running = False