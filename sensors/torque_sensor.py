import time
from PySide6.QtCore import QThread, Signal
import gpiod

class TorqueSensorWorker(QThread):
    torque_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=18, pd_sck_pin=23, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.scale_ratio = 420.0
        self._running = True

        self.request = None
        self.zero_offset = 0
        
        # Для фильтрации
        self._prev_torque = 0.0
        self._suspected_value = None
        self._suspected_prev = None
        self._max_change = 0.5  # Порог (Н·м)

    def run(self):
        try:
            print(f"[Torque BTQ-403A] Инициализация GPIO (DOUT={self.dout_pin}, SCK={self.pd_sck_pin}) via gpiod v2...")
            
            chip_path = "/dev/gpiochip4"
            try:
                gpiod.Chip(chip_path).close()
            except Exception:
                chip_path = "/dev/gpiochip0"

            config = {
                self.dout_pin: gpiod.LineSettings(direction=gpiod.line.Direction.INPUT),
                self.pd_sck_pin: gpiod.LineSettings(direction=gpiod.line.Direction.OUTPUT, output_value=gpiod.line.Value.INACTIVE)
            }

            self.request = gpiod.request_lines(
                chip_path,
                consumer="HX711_TORQUE",
                config=config
            )

            self.msleep(500)
            self.zero_offset = self._read_average(10)
            print(f"[Torque BTQ-403A] Готов. Нулевое смещение: {self.zero_offset}")
            self.zero_offset = 0

            while self._running:
                raw_val = self._read_average(3)
                if raw_val is not None:
                    val = (raw_val - self.zero_offset) / self.scale_ratio - 110
                    
                    if abs(val) < 0.05:
                        val = 0.0

                    filtered_value = self._smart_filter(val)
                    self.torque_updated.emit(filtered_value)
                
                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка чтения Torque Sensor: {e}"
            print(f"[Torque Error] {error_msg}")
            self.error_occurred.emit(error_msg)
        finally:
            self._cleanup()

    def _smart_filter(self, value):
        """Умный фильтр: отличает выброс от реального изменения"""
        diff = abs(value - self._prev_torque)
        
        if diff <= self._max_change:
            self._suspected_value = None
            self._suspected_prev = None
            self._prev_torque = value
            return value
        
        if self._suspected_value is None:
            self._suspected_value = value
            self._suspected_prev = self._prev_torque
            return self._prev_torque
        else:
            diff_back = abs(value - self._suspected_prev)
            
            if diff_back <= self._max_change:
                self._suspected_value = None
                self._suspected_prev = None
                return self._prev_torque
            else:
                self._prev_torque = self._suspected_value
                self._suspected_value = None
                self._suspected_prev = None
                return self._prev_torque

    def _read_raw(self):
        count = 0
        timeout = 100
        
        while self.request.get_value(self.dout_pin) != gpiod.line.Value.INACTIVE and timeout > 0:
            time.sleep(0.001)
            timeout -= 1

        if timeout <= 0:
            return None

        for _ in range(24):
            self.request.set_value(self.pd_sck_pin, gpiod.line.Value.ACTIVE)
            bit_val = 1 if self.request.get_value(self.dout_pin) == gpiod.line.Value.ACTIVE else 0
            count = (count << 1) | bit_val
            self.request.set_value(self.pd_sck_pin, gpiod.line.Value.INACTIVE)

        self.request.set_value(self.pd_sck_pin, gpiod.line.Value.ACTIVE)
        self.request.set_value(self.pd_sck_pin, gpiod.line.Value.INACTIVE)

        if count & 0x800000:
            count -= 0x1000000 

        return count

    def _read_average(self, times=3):
        values = []
        for _ in range(times):
            v = self._read_raw()
            if v is not None:
                values.append(v)
            time.sleep(0.002)
        return sum(values) / len(values) if values else None

    def stop(self):
        self._running = False
        self.wait()

    def _cleanup(self):
        if self.request:
            try:
                self.request.release()
            except Exception:
                pass
        print("[Torque BTQ-403A] Ресурсы gpiod освобождены.")