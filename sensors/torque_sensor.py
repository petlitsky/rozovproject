import time
from PySide6.QtCore import QThread, Signal
from hx711_gpiozero import HX711


class TorqueSensorWorker(QThread):
    # Сигнал передает крутящий момент в Н·м (или Н·см, в зависимости от калибровки)
    torque_updated = Signal(float)
    # Сигнал для передачи ошибок в GUI
    error_occurred = Signal(str)

    def __init__(self, dout_pin=18, pd_sck_pin=23, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin

        # Скалирующий коэффициент для BTQ-403A (подбирается при калибровке эталонным грузом/рычагом)
        self.scale_ratio = 0.00234  

        self._running = True
        self.scale = None

    def run(self):
        try:
            print(f"[BTQ-403A] Инициализация на пинах select_pin={self.dout_pin}, clock_pin={self.pd_sck_pin}...")
            # Задаем пины DT=18, SCK=23
            self.scale = HX711(select_pin=self.dout_pin, clock_pin=self.pd_sck_pin)

            # Пауза 2 секунды для стабилизации питания датчика
            self.msleep(2000)

            # Фиксация нулевого момента (обнуление/тарировка без нагрузки)
            init_reading = self.scale.value
            print(f"[BTQ-403A] Значение нуля зафиксировано: {init_reading}")

            while self._running:
                raw_value = self.scale.value

                if raw_value is not None:
                    # Расчет текущего крутящего момента
                    current_torque = (raw_value - init_reading) * self.scale_ratio

                    # Фильтр шума около нуля (учитываем возможный люфт/дребезг)
                    if abs(current_torque) < 0.05:
                        current_torque = 0.0

                    # Отправляем значение в GUI (float)
                    self.torque_updated.emit(float(current_torque))

                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка чтения BTQ-403A: {e}"
            print(f"[BTQ-403A Error] {error_msg}")
            self.error_occurred.emit(error_msg)
        finally:
            self._cleanup()

    def stop(self):
        """Плавная остановка потока."""
        self._running = False
        self.wait()

    def _cleanup(self):
        """Освобождение GPIO пинов."""
        if self.scale and hasattr(self.scale, "close"):
            try:
                self.scale.close()
            except Exception:
                pass
            print("[BTQ-403A] Ресурсы GPIO 18/23 успешно освобождены")