# sensors/fan_controller.py
import RPi.GPIO as GPIO
from PySide6.QtCore import QObject, Signal


class FanController(QObject):
    """Управление куллером через MOSFET IRF520N на GPIO12 (PWM)"""
    
    fan_speed_updated = Signal(int)  # скорость в %
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._pwm_pin = 12  # GPIO12
        self._pwm = None
        self._speed = 0  # 0-100%
        self._is_initialized = False
        
        self._init_gpio()
    
    def _init_gpio(self):
        """Инициализация GPIO и PWM"""
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self._pwm_pin, GPIO.OUT)
            
            # PWM на 1 кГц
            self._pwm = GPIO.PWM(self._pwm_pin, 1000)
            self._pwm.start(0)
            self._is_initialized = True
            print(f"Fan PWM инициализирован на GPIO{self._pwm_pin}")
            
        except Exception as e:
            self._is_initialized = False
            print(f"Ошибка инициализации Fan: {e}")
    
    def set_speed(self, speed: int) -> None:
        """Установка скорости вентилятора (0-100%)"""
        if not self._is_initialized:
            return
        
        # Ограничиваем значение
        speed = max(0, min(100, speed))
        self._speed = speed
        
        # DC = Duty Cycle (0-100)
        self._pwm.ChangeDutyCycle(speed)
        
        self.fan_speed_updated.emit(speed)
        print(f"Fan speed: {speed}%")
    
    def get_speed(self) -> int:
        """Получение текущей скорости"""
        return self._speed
    
    def stop(self):
        """Остановка вентилятора"""
        self.set_speed(0)
    
    def cleanup(self):
        """Очистка GPIO"""
        if self._pwm:
            self._pwm.stop()
        GPIO.cleanup(self._pwm_pin)
        print("Fan GPIO очищен")