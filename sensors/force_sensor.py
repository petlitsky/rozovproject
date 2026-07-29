import time
from PySide6.QtCore import QThread, Signal
from hx711_gpiozero import HX711


class ForceSensorWorker(QThread):
    # Сигнал передает измеренное значение силы/веса в GUI
    force_updated = Signal(float)
    # Сигнал для передачи ошибок в GUI (если датчик отключится)
    error_occurred = Signal(str)

    def __init__(self, dout_pin=24, pd_sck_pin=25, parent=None):
        super().__init__(parent)
        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.scale_ratio = 0.00234  # Ваш скалирующий коэффициент
        self._running = True
        self.scale = None

    def run(self):
        try:
            print(f"[HX711] Инициализация на пинах select_pin={self.dout_pin}, clock_pin={self.pd_sck_pin}...")
            # Передаем пины в точности, как в вашем рабочем скрипте
            self.scale = HX711(select_pin=self.dout_pin, clock_pin=self.pd_sck_pin)

            # Стабилизация датчика
            self.msleep(2000)

            # Чтение значения пустой тары (обнуление)
            init_reading = self.scale.value
            print(f"[HX711] Значение тары зафиксировано: {init_reading}")

            while self._running:
                raw_value = self.scale.value

                if raw_value is not None:
                    # Расчет чистого веса/усилия по вашей формуле
                    current_weight = (raw_value - init_reading) * self.scale_ratio

                    # Отсечение шума около нуля
                    if abs(current_weight) < 0.1:
                        current_weight = 0.0

                    # Отправка значения в основной UI поток
                    self.force_updated.emit(float(current_weight))

                # Пауза 100 мс для стабильности цикла
                self.msleep(100)

        except Exception as e:
            error_msg = f"Ошибка работы HX711: {e}"
            print(f"[HX711 Error] {error_msg}")
            self.error_occurred.emit(error_msg)
        finally:
            self._cleanup()

    def stop(self):
        """Безопасная остановка потока из главного окна GUI."""
        self._running = False
        self.wait()  # Ожидаем корректного завершения run()

    def _cleanup(self):
        """Освобождение ресурсов GPIO при закрытии."""
        if self.scale and hasattr(self.scale, "close"):
            try:
                self.scale.close()
            except Exception:
                pass
            print("[HX711] Ресурсы GPIO успешно освобождены")