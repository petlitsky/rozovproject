import time
from PySide6.QtCore import QThread, Signal
import gpiod

class TorqueSensorWorker(QThread):
    torque_updated = Signal(float)
    error_occurred = Signal(str)

    import gpiod
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal

class TorqueSensor(QThread):
    torque_updated = pyqtSignal(float)

    def __init__(self, dout_pin=18, pd_sck_pin=23, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self._running = True
        self.request = None
        self.zero_offset = 0

        # --- КАЛИБРОВОЧНАЯ ТАБЛИЦА (на основе ваших замеров и рычага 205 мм) ---
        # Длина рычага: 0.205 м. Ускорение: 9.80665 м/с²
        # Формула момента: М = (граммы / 1000) * 9.80665 * 0.205
        
        # 1. Значения, которые выдавал ваш старый код (при коэфф. 420 и zero=0)
        old_code_vals = np.array([166, 825, 836, 1024, 1184])
        
        # Восстанавливаем из них чистые сырые данные АЦП (raw_val)
        self.cal_raw = old_code_vals * 420.0
        
        # 2. Соответствующий им реальный физический момент в Н*м
        self.cal_torque = np.array([
            0.0,                               # 0 г
            (350 / 1000.0) * 9.80665 * 0.205,  # 350 г (~0.70 Н*м)
            (340 / 1000.0) * 9.80665 * 0.205,  # 340 г (~0.68 Н*м)
            (4100 / 1000.0) * 9.80665 * 0.205, # 4100 г (~8.24 Н*м)
            (4910 / 1000.0) * 9.80665 * 0.205  # 4910 г (~9.87 Н*м)
        ])
        
        # Сортируем массивы для корректной работы интерполяции
        idx = np.argsort(self.cal_raw)
        self.cal_raw = self.cal_raw[idx]
        self.cal_torque = self.cal_torque[idx]

    def run(self):
        try:
            print(f"[Torque BTQ-403A] Инициализация GPIO...")
            chip_path = "/dev/gpiochip4"
            try: gpiod.Chip(chip_path).close()
            except Exception: chip_path = "/dev/gpiochip0"

            config = {
                self.dout_pin: gpiod.LineSettings(direction=gpiod.line.Direction.INPUT),
                self.pd_sck_pin: gpiod.LineSettings(direction=gpiod.line.Direction.OUTPUT, output_value=gpiod.line.Value.INACTIVE)
            }
            self.request = gpiod.request_lines(chip_path, consumer="HX711_TORQUE", config=config)

            # При кусочной интерполяции мы не используем динамический авто-ноль, 
            # так как точка 0 г (166 * 420) уже жестко заложена в таблицу калибровки.
            print(f"[Torque BTQ-403A] Готов. Используется табличная интерполяция.")

            while self._running:
                raw_val = self._read_average(3)
                if raw_val is not None:
                    # Автоматический точный перевод сырого значения в Н*м по таблице
                    val = float(np.interp(raw_val, self.cal_raw, self.cal_torque))
                    
                    # Отсечка мелких шумов вокруг абсолютного нуля
                    if abs(val) < 0.05:
                        val = 0.0

                    self.torque_updated.emit(val)
                
                self.msleep(100)
        except Exception as e:
            print(f"Ошибка в потоке датчика: {e}")


        except Exception as e:
            error_msg = f"Ошибка чтения Torque Sensor: {e}"
            print(f"[Torque Error] {error_msg}")
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
        print("[Torque BTQ-403A] Ресурсы gpiod освобождены.")