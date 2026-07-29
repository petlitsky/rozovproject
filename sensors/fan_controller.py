import lgpio
from PySide6.QtCore import QObject, Signal


class FanController(QObject):
    fan_speed_updated = Signal(int)  # скорость в %
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._gpio_chip = 0  # Для RPi 4 / RPi 3 обычно chip 0. (Для RPi 5 используется chip 4)
        self._pwm_pin = 12   # GPIO12 (Физический пин 32)
        self._handle = None
        self._speed = 0      # 0-100%
        self._is_initialized = False
        
        self._init_gpio()
    
    def _init_gpio(self):
        try:
            # Открываем чип GPIO
            self._handle = lgpio.gpiochip_open(self._gpio_chip)
            
            # Настраиваем пин GPIO12 как ШИМ-выход
            # Частота 50 Гц — идеально для силовых ключей IRF520N
            # Изначально ставим 0% (выключен)
            lgpio.tx_pwm(self._handle, self._pwm_pin, 50, 0)
            
            self._is_initialized = True
            print(f"[FAN] Инициализация lgpio на GPIO{self._pwm_pin} прошла успешно")
            
        except Exception as e:
            self._is_initialized = False
            print(f"[FAN ERROR] Ошибка инициализации lgpio: {e}")
            print("[FAN TIP] Если используете Raspberry Pi 5, смените self._gpio_chip = 4 в коде.")

    def set_speed(self, speed: int) -> None:
        if not self._is_initialized or self._handle is None:
            print("[FAN WARN] Попытка установить скорость, но lgpio не инициализирован")
            return
        
        speed = max(0, min(100, speed))
        self._speed = speed
        
        # tx_pwm принимает (handle, pin, frequency, duty_cycle_percent)
        lgpio.tx_pwm(self._handle, self._pwm_pin, 50, float(speed))
        
        self.fan_speed_updated.emit(speed)
        print(f"[FAN] Установлена скорость: {speed}%")
    
    def get_speed(self) -> int:
        return self._speed
    
    def stop(self):
        self.set_speed(0)
    
    def cleanup(self):
        if self._handle is not None:
            # Отключаем ШИМ и освобождаем чип
            try:
                lgpio.tx_pwm(self._handle, self._pwm_pin, 50, 0)
                lgpio.gpiochip_close(self._handle)
                print("[FAN] Ресурсы lgpio успешно освобождены")
            except Exception as e:
                print(f"[FAN ERROR] Ошибка при cleanup: {e}")