import time
from PySide6.QtCore import QThread, Signal
import gpiod

class ForceSensorWorker(QThread):
    # Передает силу в Ньютонах (Н)
    force_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=24, pd_sck_pin=25, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        
        # Калибровочный коэффициент для перевода сырых отсчетов в ГРАММЫ
        self.scale_ratio = 420.0  
        self._running = True

        self.request = None
        self.zero_offset = 0

    def run(self):
        try:
            print(f"[Force Sensor] Инициализация GPIO (DOUT={self.dout_pin}, SCK={self.pd_sck_pin}) via gpiod v2...")
            
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
                consumer="HX711_FORCE",
                config=config
            )

            # Тарировка (обнуление)
            self.msleep(500)
            self.zero_offset = self._read_average(10)
            print(f"[Force Sensor] Готов. Нулевое смещение: {self.zero_offset}")

            while self._running:
                raw_val = self._read_average(3)
                if raw_val is not None:
                    # 1. Расчет массы в граммах
                    weight_grams = (raw_val) / self.scale_ratio
                    
                    # 2. Перевод граммов в Ньютоны (Н): (г / 1000) * 9.80665
                    force_newtons = (weight_grams / 1000.0) * 9.80665

                    # Отсечка мелких шумов около нуля (менее ~0.01 Н)
                    if abs(force_newtons) < 0.01:
                        force_newtons = 0.0

                    # Отправляем усилие в Ньютонах
                    self.force_updated.emit(float(force_newtons))
                
                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка чтения Force Sensor: {e}"
            print(f"[Force Error] {error_msg}")
            self.error_occurred.emit(error_msg)
        finally:
            self._cleanup()

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
        print("[Force Sensor] Ресурсы gpiod освобождены.")