# controllers/arduino_controller.py
import serial
import serial.tools.list_ports
from typing import Optional, Callable
from PySide6.QtCore import QObject, QTimer, Signal


class ArduinoController(QObject):
    """Контроллер для работы с Arduino"""
    
    # Сигналы для обновления UI
    position_updated = Signal(str, int)  # (axis, position)
    moving = Signal(str)                 # (axis)
    home_found = Signal(str)             # (axis)
    limit_reached = Signal(str, str)     # (axis, direction)
    move_done = Signal()
    disconnected = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.serial_port: Optional[serial.Serial] = None
        self.is_connected = False
        self._disconnect_shown = False
        self._timer: Optional[QTimer] = None
        
        # Обработчики для разных типов сообщений
        self._handlers = {
            "LIN_POS": self._handle_position,
            "PRE_POS": self._handle_position,
            "LIN_MOVING": lambda: self.moving.emit("LIN"),
            "PRE_MOVING": lambda: self.moving.emit("PRE"),
            "LIN_HOME_FOUND": lambda: self.home_found.emit("LIN"),
            "PRE_HOME_FOUND": lambda: self.home_found.emit("PRE"),
            "FIX_HOME_FOUND": lambda: self.home_found.emit("FIX"),
            "POST_HOME_FOUND": lambda: self.home_found.emit("POST"),
            "STOP_LIMIT_BACK": lambda: self.limit_reached.emit("LIN", "BACK"),
            "STOP_LIMIT_FORWARD": lambda: self.limit_reached.emit("LIN", "FORWARD"),
            "STOP_LIMIT_PRE_UP": lambda: self.limit_reached.emit("PRE", "UP"),
            "STOP_LIMIT_PRE_DOWN": lambda: self.limit_reached.emit("PRE", "DOWN"),
            "MOVE_DONE": lambda: self.move_done.emit(),
            "PRE_MOVE_DONE": lambda: self.move_done.emit(),
            "LIN_POS_SET": lambda: None,
            "PRE_POS_SET": lambda: None,
        }
    
    def connect(self) -> bool:
        """Подключение к Arduino"""
        ports = self._get_ports_to_try()
        
        for port in ports:
            try:
                self.serial_port = serial.Serial(port, 115200, timeout=1)
                self.is_connected = True
                self._disconnect_shown = False
                
                # Запуск таймера чтения
                self._timer = QTimer()
                self._timer.timeout.connect(self._read_serial)
                self._timer.start(10)
                
                print(f"Подключено к Arduino на {port}")
                return True
                
            except (serial.SerialException, OSError) as e:
                continue
        
        self.is_connected = False
        print("Arduino не найдена ни на одном порту")
        return False
    
    def disconnect(self) -> None:
        """Отключение от Arduino"""
        self.is_connected = False
        
        if self._timer:
            self._timer.stop()
            self._timer = None
        
        if self.serial_port and self.serial_port.is_open:
            try:
                self.serial_port.close()
            except (serial.SerialException, OSError):
                pass
        
        self.disconnected.emit()
    
    def send_command(self, command: str) -> bool:
        """Отправка команды"""
        if not self.is_connected or not self.serial_port or not self.serial_port.is_open:
            return False
        
        try:
            self.serial_port.write(f"{command}\n".encode('utf-8'))
            return True
        except (serial.SerialException, OSError, IOError):
            self.disconnect()
            return False
    
    def _read_serial(self) -> None:
        """Чтение данных из порта"""
        if not self.serial_port or not self.serial_port.is_open:
            if self.is_connected:
                self.disconnect()
            return
        
        try:
            while self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode('utf-8').strip()
                if data:
                    self._process_data(data)
                    
        except (serial.SerialException, OSError, IOError) as e:
            self.disconnect()
        except Exception as e:
            print(f"Ошибка чтения: {e}")
    
    def _process_data(self, data: str) -> None:
        """Обработка полученных данных"""
        # Проверяем на команды с параметрами (LIN_POS:123)
        for key, handler in self._handlers.items():
            if data.startswith(key + ":"):
                value = data.split(":")[1]
                if "POS" in key and key not in ["LIN_POS_SET", "PRE_POS_SET"]:
                    axis = key.split("_")[0]
                    try:
                        self.position_updated.emit(axis, int(value))
                    except ValueError:
                        pass
                else:
                    handler()
                return
            
            if data == key:
                handler()
                return
        
        # Неизвестная команда (для отладки)
        print(data)
    
    def _handle_position(self, data: str) -> None:
        """Обработка позиции"""
        # Реализовано в _process_data
        pass
    
    def _get_ports_to_try(self) -> list:
        """Получение списка портов для перебора"""
        ports = [f"COM{i}" for i in range(1, 16)]
        ports.extend(["/dev/ttyACM0", "/dev/ttyACM1", "/dev/ttyUSB0", "/dev/ttyUSB1"])
        
        try:
            available = serial.tools.list_ports.comports()
            for port in available:
                if port.device not in ports:
                    ports.append(port.device)
        except Exception:
            pass
        
        return ports