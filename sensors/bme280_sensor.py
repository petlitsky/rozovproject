# sensors/bme280_sensor.py
from PySide6.QtCore import QObject, QTimer, Signal
import random


class BME280Sensor(QObject):
    """Датчик температуры BME280 на RPi5 (заглушка)"""
    
    temperature_updated = Signal(float)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._temperature = 20.0
        self._real_sensor = False
        
        # Пытаемся подключить реальный датчик
        try:
            import smbus2
            self._bus = smbus2.SMBus(1)
            # Проверяем адрес 0x76
            try:
                self._bus.read_byte_data(0x76, 0xD0)
                self._real_sensor = True
                self._address = 0x76
                print("BME280 реальный (адрес 0x76)")
            except:
                try:
                    self._bus.read_byte_data(0x77, 0xD0)
                    self._real_sensor = True
                    self._address = 0x77
                    print("BME280 реальный (адрес 0x77)")
                except:
                    self._real_sensor = False
                    print("BME280 не найден, использую заглушку")
        except:
            self._real_sensor = False
            print("BME280 не найден, использую заглушку")
        
        self._setup_timer()
    
    def _setup_timer(self):
        """Таймер для чтения температуры каждую секунду"""
        self._timer = QTimer()
        self._timer.timeout.connect(self._read_temperature)
        self._timer.start(1000)
    
    def _read_temperature(self):
        """Чтение температуры"""
        if self._real_sensor:
            try:
                data = self._bus.read_i2c_block_data(self._address, 0xFA, 3)
                temp_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
                temp = temp_raw / 100.0
                self._temperature = temp
                self.temperature_updated.emit(temp)
                return
            except:
                pass
        
        # Заглушка (20-25°C)
        self._temperature = 20.0 + (random.random() * 5.0)
        self.temperature_updated.emit(self._temperature)
    
    def get_temperature(self) -> float:
        return self._temperature