import serial
import serial.tools.list_ports
from typing import Optional
from PySide6.QtCore import QObject, QTimer, Signal


class ArduinoController(QObject):
    position_updated = Signal(str, int)
    moving = Signal(str)
    home_found = Signal(str)
    limit_reached = Signal(str, str)
    disconnected = Signal()
    speed_updated = Signal(str, int)
    current_updated = Signal(float)  # Сигнал для тока

    def __init__(self, parent=None):
        super().__init__(parent)

        self.serial_port: Optional[serial.Serial] = None
        self.is_connected = False
        self._disconnect_shown = False
        self._timer: Optional[QTimer] = None

        # Для фильтрации тока
        self._prev_current = 0.0
        self._filter_threshold = 0.3  # Порог изменения для фильтра (А)
        self._consecutive_count = 0   # Счетчик одинаковых отклонений
        self._filter_window = 5       # Окно для подтверждения изменения

        self._handlers = {
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
        }

    def connect(self) -> bool:
        ports = self._get_ports_to_try()

        for port in ports:
            try:
                self.serial_port = serial.Serial(port, 115200, timeout=1)
                self.is_connected = True
                self._disconnect_shown = False

                self._timer = QTimer()
                self._timer.timeout.connect(self._read_serial)
                self._timer.start(10)

                return True

            except (serial.SerialException, OSError):
                continue

        self.is_connected = False
        return False

    def disconnect(self) -> None:
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
        if not self.is_connected or not self.serial_port or not self.serial_port.is_open:
            return False

        try:
            self.serial_port.write(f"{command}\n".encode('utf-8'))
            print(f"[TX -> Arduino]: {command}")
            return True
        except (serial.SerialException, OSError, IOError):
            self.disconnect()
            return False

    def _read_serial(self) -> None:
        if not self.serial_port or not self.serial_port.is_open:
            if self.is_connected:
                self.disconnect()
            return

        try:
            while self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode('utf-8').strip()
                if data:
                    self._process_data(data)
                    print(f"[RX <- Arduino]: {data}")

        except (serial.SerialException, OSError, IOError):
            self.disconnect()
 
    def _filter_current_spike(self, value):
        """
        Фильтр выбросов для тока.
        Если значение резко отличается от предыдущего - проверяем несколько раз.
        """
        diff = abs(value - self._prev_current)
        
        # Если изменение больше порога - это потенциальный выброс
        if diff > self._filter_threshold:
            # Увеличиваем счетчик подозрительных значений
            self._consecutive_count += 1
            
            # Если подозрительных значений больше окна - это реальное изменение
            if self._consecutive_count >= self._filter_window:
                self._consecutive_count = 0
                self._prev_current = value
                return value
            else:
                # Возвращаем предыдущее значение (фильтруем выброс)
                return self._prev_current
        else:
            # Нормальное изменение - сбрасываем счетчик
            self._consecutive_count = 0
            self._prev_current = value
            return value

    def _process_data(self, data: str) -> None:
        # 1. Обработка команд без параметров
        if data in self._handlers:
            self._handlers[data]()
            return

        # 2. Обработка команд с параметрами вида 'КЛЮЧ:ЗНАЧЕНИЕ'
        if ":" in data:
            parts = data.split(":", 1)
            key, val = parts[0], parts[1]

            # Позиции
            if key in ("LIN_POS", "PRE_POS"):
                axis = key.split("_")[0]
                try:
                    self.position_updated.emit(axis, int(val))
                except ValueError:
                    pass
                return

            # Ток - с фильтрацией
            if key == "CURRENT":
                try:
                    raw_current = float(val)
                    # Применяем фильтрацию
                    filtered_current = self._filter_current_spike(raw_current)
                    self.current_updated.emit(filtered_current)
                except ValueError:
                    pass
                return

            # Скорости
            if "_SPEED_CURRENT" in key or "_SPEED_SET" in key:
                axis = key.split("_")[0]
                try:
                    self.speed_updated.emit(axis, int(val))
                except ValueError:
                    pass
                return

    def set_current_filter_threshold(self, threshold: float):
        """Установка порога фильтрации тока (А)"""
        self._filter_threshold = threshold

    def set_current_filter_window(self, window: int):
        """Установка окна фильтрации тока (количество измерений)"""
        self._filter_window = window

    def _get_ports_to_try(self) -> list:
        ports = [f"COM{i}" for i in range(1, 16)]
        ports.extend(["/dev/ttyACM0", "/dev/ttyACM1", "/dev/ttyUSB0", "/dev/ttyUSB1"])
        return ports