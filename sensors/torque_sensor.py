import time
from PySide6.QtCore import QThread, Signal
import gpiod
import numpy as np

class TorqueSensorWorker(QThread):
    torque_updated = Signal(float)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=18, pd_sck_pin=23, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        
        # --- КАЛИБРОВОЧНАЯ ТАБЛИЦА (Рычаг 205 мм = 0.205 м) ---
        # 1. Ваши экспериментальные точки (значения "Н*м" из старого кода при коэфф. 420)
        old_vals = np.array([166.0, 825.0, 1184.0, 1184.0, 836.0])
        
        # Переводим старые значения обратно в чистый сырой сыгнал АЦП (raw_val)
        self.cal_raw = old_vals * 420.0
        
        # 2. Рассчитываем точный физический крутящий момент (М = F * L = (г / 1000) * 9.80665 * 0.205)
        # Соответствует точкам: 0г, 350г, 4100г, 4910г, 340г
        self.cal_torque = np.array([
            0.0,
            (350.0 / 1000.0) * 9.80665 * 0.205,
            (4100.0 / 1000.0) * 9.80665 * 0.205,
            (4910.0 / 1000.0) * 9.80665 * 0.205,
            (340.0 / 1000.0) * 9.80665 * 0.205
        ])
        
        # Сортируем массивы по возрастанию сигнала АЦП для правильной интерполяции
        idx = np.argsort(self.cal_raw)
        self.cal_raw = self.cal_raw[idx]
        self.cal_torque = self.cal_torque[idx]

        self._running = True
        self.request = None

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

            # Ожидание стабилизации АЦП
            self.msleep(500)
            print(f"[Torque BTQ-403A] Готов. Используется табличная интерполяция Н*м.")

            while self._running:
                raw_val = self._read_average(3)
                if raw_val is not None:
                    # Умножаем сырые данные со считывателя (если ваш метод _read_average 
                    # возвращает чистый АЦП, а не деленный на 420. Если деленный — убрать "* 420.0")
                    # Переводим в Н*м по калибровочной сетке:
                    val = float(np.interp(raw_val, self.cal_raw, self.cal_torque))
                    
                    # Отсечка мелких шумов около нуля (менее 0.05 Н*м)
                    if abs(val) < 0.05:
                        val = 0.0

                    self.torque_updated.emit(val)
                
                self.msleep(100)
                
        except Exception as e:
            print(f"[Torque BTQ-403A] Ошибка выполнения потока: {e}")

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