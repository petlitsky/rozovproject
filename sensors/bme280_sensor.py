# sensors/bme280_sensor.py
import board
import busio
import adafruit_bme280
from PySide6.QtCore import QObject, QTimer, Signal


class BME280Sensor(QObject):
    """Датчик температуры BME280 на RPi5"""
    
    temperature_updated = Signal(float)  # температура в °C
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._sensor = None
        self._is_connected = False
        
        self._init_sensor()
        self._setup_timer()
    
    def _init_sensor(self) -> None:
        """Инициализация BME280"""
        try:
            i2c = busio.I2C(board.SCL, board.SDA)
            self._sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
            self._is_connected = True
            print("BME280 подключен")
        except Exception as e:
            self._is_connected = False
            print(f"BME280 не найден: {e}")
    
    def _setup_timer(self) -> None:
        """Таймер для чтения температуры каждую секунду"""
        self._timer = QTimer()
        self._timer.timeout.connect(self._read_temperature)
        self._timer.start(1000)
    
    def _read_temperature(self) -> None:
        """Чтение температуры"""
        if not self._is_connected or self._sensor is None:
            return
        
        try:
            temp = self._sensor.temperature
            self.temperature_updated.emit(temp)
        except Exception as e:
            print(f"Ошибка чтения температуры: {e}")
    
    def get_temperature(self) -> float:
        """Получение текущей температуры"""
        if self._is_connected and self._sensor is not None:
            try:
                return self._sensor.temperature
            except:
                return 0.0
        return 0.0