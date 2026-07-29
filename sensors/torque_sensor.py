import time
from PySide6.QtCore import QThread, Signal
import gpiod


class TorqueSensorWorker(QThread):
    torque_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=12, pd_sck_pin=16, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.scale_ratio = 420.0  # Калибровочный коэффициент для BTQ-403A
        self._running = True

        self.chip = None
        self.dout_line = None
        self.sck_line = None
        self.zero_offset = 0

    def _get_chip(self):
        """Универсальное открытие gpiochip для Pi 4 и Pi 5"""
        for chip_path in ["/dev/gpiochip4", "/dev/gpiochip0", "gpiochip4", "gpiochip0"]:
            try:
                return gpiod.Chip(chip_path)
            except Exception:
                continue
        raise RuntimeError("Не удалось найти доступный gpiochip в системе")

    def run(self):
        try:
            print(f"[Torque BTQ-403A] Инициализация GPIO (DOUT={self.dout_pin}, SCK={self.pd_sck_pin})...")
            self.chip = self._get_chip()

            self.dout_line = self.chip.get_line(self.dout_pin)
            self.sck_line = self.chip.get_line(self.pd_sck_pin)

            self.dout_line.request(consumer="HX711_TORQUE_DOUT", type=gpiod.LINE_REQ_DIR_IN)
            self.sck_line.request(consumer="HX711_TORQUE_SCK", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

            # Тарировка (обнуление)
            self.msleep(500)
            self.zero_offset = self._read_average(10)
            print(f"[Torque BTQ-403A] Готов. Нулевое смещение: {self.zero_offset}")

            while self._running:
                raw_val = self._read_average(3)
                if raw_val is not None:
                    val = (raw_val - self.zero_offset) / self.scale_ratio
                    
                    if abs(val) < 0.05:
                        val = 0.0

                    self.torque_updated.emit(float(val))
                
                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка чтения Torque Sensor: {e}"
            print(f"[Torque Error] {error_msg}")
            self.error_occurred.emit(error_msg)
        finally:
            self._cleanup()

    def _read_raw(self):
        count = 0
        timeout = 100
        while self.dout_line.get_value() != 0 and timeout > 0:
            time.sleep(0.001)
            timeout -= 1

        if timeout <= 0:
            return None

        for _ in range(24):
            self.sck_line.set_value(1)
            count = (count << 1) | self.dout_line.get_value()
            self.sck_line.set_value(0)

        self.sck_line.set_value(1)
        self.sck_line.set_value(0)

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
        try:
            if self.dout_line:
                self.dout_line.release()
            if self.sck_line:
                self.sck_line.release()
            if self.chip:
                self.chip.close()
        except Exception:
            pass
        print("[Torque BTQ-403A] Ресурсы gpiod освобождены.")