# sensors/force_sensor.py
from PySide6.QtCore import QThread, Signal
import time
# Использование gpiozero снизу решает проблему совместимости с Pi 5
from hx711_gpiozero import HX711 

class ForceSensorWorker(QThread):
    force_updated = Signal(float)
    
    def __init__(self, dout_pin=24, pd_sck_pin=23):
        super().__init__()
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self._running = True
        self.hx = None

    def run(self):
        try:
            # Инициализация HX711
            self.hx = HX711(dout=self.dout_pin, pd_sck=self.pd_sck_pin)
            # Установка калибровочного коэффициента (подберите под свои весы)
            self.hx.set_reference_unit(420) 
            self.hx.reset()
            self.hx.tare()

            while self._running:
                val = self.hx.get_weight(5)
                self.force_updated.emit(val)
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Ошибка чтения HX711: {e}")

    def stop(self):
        self._running = False