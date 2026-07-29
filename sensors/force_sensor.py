import time
from PySide6.QtCore import QObject, QThread, Signal


class ForceSensorWorker(QThread):
    """Фоновый поток для опроса тензодатчика TCF-715A через HX711"""

    force_updated = Signal(float)

    def __init__(self, dout_pin=24, pd_sck_pin=23, parent=None):
        super().__init__(parent)
        self._dout_pin = dout_pin
        self._pd_sck_pin = pd_sck_pin
        self._running = False

        # Параметры калибровки (нужно будет настроить под ваш TCF-715A)
        self.reference_unit = 1.0  # Коэффициент масштабирования
        self.offset = 0  # Смещение нуля (Тара)
        self._hx = None

    def _init_hx711(self) -> bool:
        try:
            from hx711 import HX711

            # Инициализация с передачей GPIO24 (DT) и GPIO23 (SCK)
            self._hx = HX711(
                dout_pin=self._dout_pin, pd_sck_pin=self._pd_sck_pin
            )
            self._hx.set_scale_ratio(self.reference_unit)
            self._hx.reset()
            self._hx.tare()
            print(
                f"[HX711] Инициализация успешна (DT: GPIO{self._dout_pin}, SCK: GPIO{self._pd_sck_pin})"
            )
            return True
        except Exception as e:
            print(f"[FORCE SENSOR ERROR] Ошибка инициализации HX711: {e}")
            return False

    def run(self):
        if not self._init_hx711():
            return

        self._running = True
        while self._running:
            try:
                # Получаем среднее значение из 3 замеров для сглаживания шума
                raw_val = self._hx.get_data_mean(readings=3)
                if raw_val is not None and raw_val is not False:
                    force_value = (raw_val - self.offset) / self.reference_unit
                    self.force_updated.emit(round(force_value, 2))
            except Exception as e:
                print(f"[FORCE SENSOR ERROR] Ошибка чтения данных: {e}")

            time.sleep(0.1)

    def tare(self):
        """Сброс текущего показания в 0 (обнуление/тара)"""
        if self._hx:
            try:
                self.offset = self._hx.get_data_mean(readings=10) or 0
                print(f"[FORCE SENSOR] Выполнена тара. Новый offset: {self.offset}")
            except Exception as e:
                print(f"[FORCE SENSOR ERROR] Ошибка выполнения тары: {e}")

    def stop(self):
        self._running = False
        self.wait()
        if self._hx:
            try:
                self._hx.power_down()
                self._hx.power_up()
            except Exception:
                pass