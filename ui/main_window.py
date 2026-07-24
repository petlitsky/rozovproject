# ui/main_window.py
import sys
from datetime import datetime
from typing import Optional
import subprocess

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QSize

from main_ui import Ui_MainWindow
from ui.dialogs import PasswordDialog, HomingDialog, ErrorDialog, show_error
from controllers.arduino_controller import ArduinoController
from controllers.manual_controls import ManualControls
from models.config import Config
from utils.logger import Logger
from sensors.bme280_sensor import BME280Sensor
from sensors.fan_controller import FanController


class MainWindow(QMainWindow):
    """Главное окно приложения"""
    
    def __init__(self):
        super().__init__()
        
        # Инициализация UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()
        
        # Инициализация компонентов
        self.config = Config()
        self.arduino = ArduinoController(self)
        self.bme280 = BME280Sensor(self)
        self.fan = FanController(self)
        self.loggers = self._create_loggers()
        self.manual = ManualControls(self)
        
        # Состояние
        self.homing_dialog: Optional[HomingDialog] = None
        self.animation: Optional[QPropertyAnimation] = None
        self.disconnect_shown = False
        self._is_closing = False
        
        # Переменные для клавиатуры
        self.keyboard_process = None
        self.keyboard_visible = False
        
        # Настройка UI
        self._setup_ui()
        self._setup_connections()
        self._setup_timer()
        self._setup_keyboard_triggers()
        
        # Подключение к Arduino
        QTimer.singleShot(500, self._connect_arduino)
    
    def _create_loggers(self) -> dict:
        """Создание логгеров для каждой вкладки"""
        return {
            'lin': Logger(self.ui.plainLogLin),
            'fix': Logger(self.ui.plainLogFix),
            'pre': Logger(self.ui.plainLogPre),
            'post': Logger(self.ui.plainLogPost),
        }
    
    def _setup_ui(self) -> None:
        """Настройка UI элементов"""
        # Кнопки главного меню
        main_buttons = [
            self.ui.btnAutoMode,
            self.ui.btnManualMode,
            self.ui.btnCalibration,
            self.ui.btnDebug,
            self.ui.btnSettings
        ]
        for btn in main_buttons:
            btn.setCheckable(True)
        
        # Кнопки подменю
        sub_buttons = [
            self.ui.btnLinear,
            self.ui.btnFixation,
            self.ui.btnPreCrimp,
            self.ui.btnPostCrimp
        ]
        for btn in sub_buttons:
            btn.setCheckable(True)
        
        # Начальное состояние
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.btnCalibration.setChecked(True)
        self.ui.subMenu.setVisible(False)
        self.ui.subMenu.setMaximumSize(QSize(16777215, 0))
        
        # Загрузка значений из конфига
        self._load_saved_values()
    
    def _setup_connections(self) -> None:
        """Настройка сигналов и слотов"""
        # Выход
        self.ui.btnExit.clicked.connect(self.close)
        
        # Кнопки главного меню
        self.ui.btnAutoMode.clicked.connect(lambda: self._on_main_button_clicked(0))
        self.ui.btnManualMode.clicked.connect(lambda: self._on_main_button_clicked(1))
        self.ui.btnCalibration.clicked.connect(lambda: self._on_main_button_clicked(2))
        self.ui.btnDebug.clicked.connect(lambda: self._on_main_button_clicked(3))
        self.ui.btnSettings.clicked.connect(lambda: self._on_main_button_clicked(4))
        
        # Кнопки подменю
        self.ui.btnLinear.clicked.connect(lambda: self._on_sub_button_clicked(0))
        self.ui.btnFixation.clicked.connect(lambda: self._on_sub_button_clicked(1))
        self.ui.btnPreCrimp.clicked.connect(lambda: self._on_sub_button_clicked(2))
        self.ui.btnPostCrimp.clicked.connect(lambda: self._on_sub_button_clicked(3))
        
        # Кнопки калибровки
        for btn_name in ['btnLinToCalib', 'btnLinToCalib_2', 'btnLinToCalib_3', 'btnLinToCalib_5']:
            if hasattr(self.ui, btn_name):
                getattr(self.ui, btn_name).clicked.connect(self._open_calibration)
        
        # Сигналы Arduino
        self.arduino.position_updated.connect(self._update_position)
        self.arduino.moving.connect(self._on_moving)
        self.arduino.home_found.connect(self._on_home_found)
        self.arduino.limit_reached.connect(self._on_limit_reached)
        self.arduino.move_done.connect(self._on_move_done)
        self.arduino.disconnected.connect(self._handle_disconnect)
        
        # Сигналы BME280
        self.bme280.temperature_updated.connect(self._update_temperature)
        
        # Сигналы Fan
        self.fan.fan_speed_updated.connect(self._update_fan_speed)
    
    def _setup_keyboard_triggers(self):
        """Настройка полей для вызова клавиатуры"""
        keyboard_fields = [
            self.ui.tempMin,
            self.ui.tempMax,
            self.ui.startSpeed,
            self.ui.exLinPos,
            self.ui.exFixPos,
            self.ui.exPrePos,
            self.ui.exPostPos,
        ]
        
        for field in keyboard_fields:
            if field and hasattr(field, 'mousePressEvent'):
                field.original_mouse_press = field.mousePressEvent
                field.mousePressEvent = self._create_keyboard_handler(field)
    
    def _create_keyboard_handler(self, widget):
        def handler(event):
            self.toggle_keyboard()
            if hasattr(widget, 'original_mouse_press'):
                widget.original_mouse_press(event)
        return handler
    
    def show_keyboard(self):
        """Показать цифровую клавиатуру"""
        if self.keyboard_process is None or self.keyboard_process.poll() is not None:
            try:
                self.keyboard_process = subprocess.Popen(["matchbox-keyboard", "-i", "-v"])
                self.keyboard_visible = True
            except FileNotFoundError:
                try:
                    self.keyboard_process = subprocess.Popen(["onboard", "--xid"])
                    self.keyboard_visible = True
                except:
                    pass
    
    def hide_keyboard(self):
        """Скрыть клавиатуру"""
        if self.keyboard_process and self.keyboard_process.poll() is None:
            self.keyboard_process.terminate()
            self.keyboard_process = None
            self.keyboard_visible = False
    
    def toggle_keyboard(self):
        """Переключить состояние клавиатуры"""
        if self.keyboard_visible:
            self.hide_keyboard()
        else:
            self.show_keyboard()
    
    def _setup_timer(self) -> None:
        """Настройка таймера для даты/времени"""
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_datetime)
        self.timer.start(1000)
        self._update_datetime()
    
    def _update_datetime(self) -> None:
        """Обновление даты и времени"""
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        if hasattr(self.ui, 'lblDate'):
            self.ui.lblDate.setText(now)
    
    def _update_temperature(self, temp: float) -> None:
        """Обновление температуры в lblTemp"""
        self.ui.lblTemp.setText(f"Температура: {temp:.1f}°C")
    
    def _update_fan_speed(self, speed: int) -> None:
        """Обновление скорости куллера в lblFanSpeed"""
        self.ui.lblFanSpeed.setText(f"Скорость куллера: {speed}%")
    
    def _load_saved_values(self) -> None:
        """Загрузка сохраненных значений из конфига"""
        speeds = [
            ('lin_speed', self.ui.linSpeed, self.ui.lblLinSpeed, "Скорость перемещения: {}%"),
            ('fix_speed', self.ui.fixSpeed, self.ui.lblFixSpeed, "Скорость зажатия: {}%"),
            ('pre_speed', self.ui.preSpeed, self.ui.lblPreSpeed, "Скорость перемещения: {}%"),
            ('post_speed', self.ui.postSpeed, self.ui.lblPostSpeed, "Скорость зажатия: {}%"),
        ]
        
        for key, slider, label, template in speeds:
            value = self.config.get(key, 30)
            slider.setValue(value)
            label.setText(template.format(value))
        
        # Fan speed если есть
        if hasattr(self.ui, 'fanSpeed'):
            fan_value = self.config.get('fan_speed', 50)
            self.ui.fanSpeed.setValue(fan_value)
            if hasattr(self.ui, 'lblFanSpeed'):
                self.ui.lblFanSpeed.setText(f"Скорость куллера: {fan_value}%")
    
    def _connect_arduino(self) -> None:
        """Подключение к Arduino"""
        if not self.arduino.connect():
            show_error(self, "Ошибка подключения", "Arduino не найдена!\nПроверьте подключение и порт.")
            return
        
        # Отправляем сохраненные значения
        QTimer.singleShot(300, self._send_saved_values)
    
    def _send_saved_values(self) -> None:
        """Отправка сохраненных значений на Arduino"""
        # Скорости
        lin_speed = self.config.get('lin_speed', 30)
        fix_speed = self.config.get('fix_speed', 30)
        pre_speed = self.config.get('pre_speed', 30)
        post_speed = self.config.get('post_speed', 30)
        
        self.arduino.send_command(f"LIN_SPEED:{lin_speed}")
        self.arduino.send_command(f"FIX_SPEED:{fix_speed}")
        self.arduino.send_command(f"PRE_SPEED:{pre_speed}")
        self.arduino.send_command(f"POST_SPEED:{post_speed}")
        
        # Позиции
        lin_pos = self.config.get('lin_position', 0)
        pre_pos = self.config.get('pre_position', 0)
        
        self.arduino.send_command(f"LIN_SET_POS:{lin_pos}")
        self.arduino.send_command(f"PRE_SET_POS:{pre_pos}")
        
        self.loggers['lin'].info(f"Загружены настройки: скорость {lin_speed}%, позиция {lin_pos} мм")
        self.loggers['pre'].info(f"Загружены настройки: скорость {pre_speed}%, позиция {pre_pos} мм")
    
    # ===== Обработчики кнопок главного меню =====
    
    def _on_main_button_clicked(self, index: int) -> None:
        """Обработка клика по кнопке главного меню"""
        self._clear_all_selection()
        
        buttons = [
            self.ui.btnAutoMode,
            self.ui.btnManualMode,
            self.ui.btnCalibration,
            self.ui.btnDebug,
            self.ui.btnSettings
        ]
        
        if index == 1:  # Ручной режим
            self._toggle_submenu(True)
        else:
            self._toggle_submenu(False)
        
        buttons[index].setChecked(True)
        self._switch_page(index)
    
    def _on_sub_button_clicked(self, index: int) -> None:
        """Обработка клика по кнопке подменю"""
        for btn in [self.ui.btnLinear, self.ui.btnFixation, self.ui.btnPreCrimp, self.ui.btnPostCrimp]:
            btn.setChecked(False)
        
        sub_buttons = [self.ui.btnLinear, self.ui.btnFixation, self.ui.btnPreCrimp, self.ui.btnPostCrimp]
        sub_buttons[index].setChecked(True)
        
        self.ui.btnManualMode.setChecked(True)
        self._switch_page(5 + index)
    
    def _open_calibration(self) -> None:
        """Открытие калибровки"""
        self._clear_all_selection()
        self.ui.btnCalibration.setChecked(True)
        self._toggle_submenu(False)
        self._switch_page(2)
    
    def _clear_all_selection(self) -> None:
        """Сброс выбора всех кнопок"""
        main_buttons = [
            self.ui.btnAutoMode,
            self.ui.btnManualMode,
            self.ui.btnCalibration,
            self.ui.btnDebug,
            self.ui.btnSettings
        ]
        for btn in main_buttons:
            btn.setChecked(False)
        
        sub_buttons = [
            self.ui.btnLinear,
            self.ui.btnFixation,
            self.ui.btnPreCrimp,
            self.ui.btnPostCrimp
        ]
        for btn in sub_buttons:
            btn.setChecked(False)
    
    def _toggle_submenu(self, show: bool) -> None:
        """Показать/скрыть подменю с анимацией"""
        if self.animation:
            self.animation.stop()
            self.animation = None
        
        if show:
            self.ui.subMenu.setVisible(True)
            self.animation = QPropertyAnimation(self.ui.subMenu, b"maximumSize")
            self.animation.setDuration(200)
            self.animation.setEasingCurve(QEasingCurve.Type.OutQuad)
            self.animation.setEndValue(QSize(16777215, 160))
            self.animation.start()
        else:
            self.animation = QPropertyAnimation(self.ui.subMenu, b"maximumSize")
            self.animation.setDuration(200)
            self.animation.setEasingCurve(QEasingCurve.Type.InQuad)
            self.animation.setEndValue(QSize(16777215, 0))
            self.animation.finished.connect(lambda: self.ui.subMenu.setVisible(False))
            self.animation.start()
            
            for btn in [self.ui.btnLinear, self.ui.btnFixation, self.ui.btnPreCrimp, self.ui.btnPostCrimp]:
                btn.setChecked(False)
    
    def _switch_page(self, index: int) -> None:
        """Переключение страницы"""
        if hasattr(self.ui, 'stackedWidget'):
            self.ui.stackedWidget.setCurrentIndex(index)
            self._update_page_values(index)
    
    def _update_page_values(self, index: int) -> None:
        """Обновление значений при переключении страницы"""
        if index in (5, 1):  # Linear
            if self.arduino.is_connected:
                self.arduino.send_command("GET_POS")
        
        elif index == 6:  # Fixation
            if self.arduino.is_connected:
                self.arduino.send_command("GET_POS")
        
        elif index == 7:  # PreCrimp
            if self.arduino.is_connected:
                self.arduino.send_command("GET_POS")
            pre_pos = self.config.get('pre_position', 0)
            self.ui.lblPrePos.setText(f"{pre_pos} мм")
            self.ui.lblPrePosMan.setText(f"{pre_pos} мм")
        
        elif index == 8:  # PostCrimp
            if self.arduino.is_connected:
                self.arduino.send_command("GET_POS")
    
    # ===== Обработчики сигналов Arduino =====
    
    def _update_position(self, axis: str, position: int) -> None:
        """Обновление позиции"""
        if axis == "LIN":
            self.ui.lblLinPos.setText(f"{position} мм")
            self.ui.lblLinPosMan.setText(f"{position} мм")
            self.config.set("lin_position", position)
        elif axis == "PRE":
            self.ui.lblPrePos.setText(f"{position} мм")
            self.ui.lblPrePosMan.setText(f"{position} мм")
            self.config.set("pre_position", position)
    
    def _on_moving(self, axis: str) -> None:
        """Обновление статуса движения"""
        if axis == "LIN":
            self.ui.lblLinPos.setText("MOVING...")
            self.ui.lblLinPosMan.setText("MOVING...")
        elif axis == "PRE":
            self.ui.lblPrePos.setText("MOVING...")
            self.ui.lblPrePosMan.setText("MOVING...")
    
    def _on_home_found(self, axis: str) -> None:
        """Обработка найденного дома"""
        messages = {
            "LIN": ("Дом линейного перемещения найден!", "lin"),
            "PRE": ("Дом предобжима найден!", "pre"),
            "FIX": ("Дом фиксации найден!", "fix"),
            "POST": ("Дом постобжима найден!", "post"),
        }
        
        if axis in messages:
            msg, logger_key = messages[axis]
            self.loggers[logger_key].info(msg)
            print(msg)
            
            if axis in ("LIN", "PRE"):
                if axis == "LIN":
                    self.ui.lblLinPos.setText("0 мм")
                    self.ui.lblLinPosMan.setText("0 мм")
                else:
                    self.ui.lblPrePos.setText("0 мм")
                    self.ui.lblPrePosMan.setText("0 мм")
                self.config.set("lin_position" if axis == "LIN" else "pre_position", 0)
            
            self._close_homing_dialog()
    
    def _on_limit_reached(self, axis: str, direction: str) -> None:
        """Обработка концевика"""
        messages = {
            ("LIN", "BACK"): ("Достигнут концевик НАЗАД", "lin"),
            ("LIN", "FORWARD"): ("Достигнут концевик ВПЕРЕД", "lin"),
            ("PRE", "UP"): ("Достигнут концевик предобжима ВВЕРХ", "pre"),
            ("PRE", "DOWN"): ("Достигнут концевик предобжима ВНИЗ", "pre"),
        }
        
        if (axis, direction) in messages:
            msg, logger_key = messages[(axis, direction)]
            self.loggers[logger_key].error(msg)
            self._close_homing_dialog()
    
    def _on_move_done(self) -> None:
        """Обработка завершения движения"""
        self.loggers['lin'].info("Перемещение завершено")
        print("Перемещение завершено")
    
    def _handle_disconnect(self) -> None:
        """Обработка отключения Arduino"""
        if self._is_closing:
            return
        
        if self.disconnect_shown:
            return
        
        self.disconnect_shown = True
        self._close_homing_dialog()
        
        self.loggers['lin'].error("Arduino отключена!")
        print("Arduino отключена!")
        
        show_error(self, "Потеря соединения", "Arduino отключена!\nПроверьте подключение.")
    
    # ===== Утилиты для диалогов =====
    
    def show_homing_dialog(self, text: str = "Идет поиск дома...") -> None:
        """Показать диалог хоуминга"""
        if not self.arduino.is_connected:
            return
        
        if self.homing_dialog is None or not self.homing_dialog.isVisible():
            self.homing_dialog = HomingDialog(self, text)
            self.homing_dialog.show()
    
    def _close_homing_dialog(self) -> None:
        """Закрыть диалог хоуминга"""
        if self.homing_dialog and self.homing_dialog.isVisible():
            self.homing_dialog.accept()
            self.homing_dialog = None
    
    # ===== Управление скоростью =====
    
    def set_lin_speed(self, value: int) -> None:
        """Установка скорости линейного перемещения"""
        self.config.set("lin_speed", value)
        self.arduino.send_command(f"LIN_SPEED:{value}")
        self.loggers['lin'].info(f"Установлена скорость: {value}%")
    
    def set_fix_speed(self, value: int) -> None:
        """Установка скорости фиксации"""
        self.config.set("fix_speed", value)
        self.arduino.send_command(f"FIX_SPEED:{value}")
        self.loggers['fix'].info(f"Установлена скорость зажатия: {value}%")
    
    def set_pre_speed(self, value: int) -> None:
        """Установка скорости предобжима"""
        self.config.set("pre_speed", value)
        self.arduino.send_command(f"PRE_SPEED:{value}")
        self.loggers['pre'].info(f"Установлена скорость: {value}%")
    
    def set_post_speed(self, value: int) -> None:
        """Установка скорости постобжима"""
        self.config.set("post_speed", value)
        self.arduino.send_command(f"POST_SPEED:{value}")
        self.loggers['post'].info(f"Установлена скорость зажатия: {value}%")
    
    def set_fan_speed(self, value: int) -> None:
        """Установка скорости куллера"""
        self.config.set("fan_speed", value)
        self.fan.set_speed(value)
        self.loggers['lin'].info(f"Установлена скорость куллера: {value}%")
    
    # ===== Управление линейным перемещением =====
    
    def lin_forward_start(self) -> None:
        self.loggers['lin'].info("Нажата кнопка ВПЕРЕД (линейный)")
        self.arduino.send_command("LIN_FORWARD_START")
    
    def lin_back_start(self) -> None:
        self.loggers['lin'].info("Нажата кнопка НАЗАД (линейный)")
        self.arduino.send_command("LIN_BACK_START")
    
    def lin_stop(self) -> None:
        self.loggers['lin'].info("Остановка линейного перемещения")
        self.arduino.send_command("LIN_STOP")
    
    def lin_home(self) -> None:
        self.loggers['lin'].info("Запуск поиска дома (линейный)")
        self.show_homing_dialog("Поиск дома линейного перемещения...")
        self.arduino.send_command("LIN_HOME_START")
        print("Поиск дома линейного перемещения...")
    
    def lin_reset_position(self) -> None:
        self.loggers['lin'].info("Сброс позиции в 0")
        self.ui.lblLinPos.setText("0 мм")
        self.ui.lblLinPosMan.setText("0 мм")
        self.config.set("lin_position", 0)
        print("Позиция сброшена в 0")
    
    def lin_move_steps(self, mm: float) -> None:
        """Перемещение на заданное расстояние"""
        steps = int(mm * 100)
        direction = "вперед" if steps > 0 else "назад"
        self.arduino.send_command(f"LIN_MOVE:{steps}")
        self.loggers['lin'].info(f"Перемещение {direction} на {abs(mm)} мм ({abs(steps)} шагов)")
    
    def lin_back_exact(self) -> None:
        """Точное перемещение назад"""
        try:
            mm = self.ui.exLinPos.value()
            if mm > 0:
                steps = int(mm * 100)
                self.arduino.send_command(f"LIN_MOVE:{-steps}")
                self.loggers['lin'].info(f"Точное перемещение назад: {mm} мм ({steps} шагов)")
                self.ui.exLinPos.setValue(0)
        except ValueError:
            self.loggers['lin'].error("Ошибка точного перемещения назад")
    
    def lin_forward_exact(self) -> None:
        """Точное перемещение вперед"""
        try:
            mm = self.ui.exLinPos.value()
            if mm > 0:
                steps = int(mm * 100)
                self.arduino.send_command(f"LIN_MOVE:{steps}")
                self.loggers['lin'].info(f"Точное перемещение вперед: {mm} мм ({steps} шагов)")
                self.ui.exLinPos.setValue(0)
        except ValueError:
            self.loggers['lin'].error("Ошибка точного перемещения вперед")
    
    # ===== Сохранение позиций =====
    
    def _get_current_lin_position(self) -> int:
        """Получение текущей позиции линейного перемещения"""
        text = self.ui.lblLinPos.text().replace(" мм", "").replace("MOVING...", "")
        try:
            return int(text) if text else 0
        except ValueError:
            return 0
    
    def save_lin_position_1(self) -> None:
        pos = self._get_current_lin_position()
        self.config.set("lin_pos1", pos)
        self.loggers['lin'].info(f"Сохранена позиция 1: {pos} мм")
        print(f"Позиция 1 сохранена: {pos} мм")
    
    def save_lin_position_2(self) -> None:
        pos = self._get_current_lin_position()
        self.config.set("lin_pos2", pos)
        self.loggers['lin'].info(f"Сохранена позиция 2: {pos} мм")
        print(f"Позиция 2 сохранена: {pos} мм")
    
    def go_to_lin_position(self, pos_num: int) -> None:
        """Переход к сохраненной позиции"""
        target = self.config.get(f"lin_pos{pos_num}", 0)
        current = self._get_current_lin_position()
        
        diff = target - current
        if diff == 0:
            self.loggers['lin'].info(f"Уже на позиции {pos_num}: {target} мм")
            return
        
        steps = diff * 100
        self.arduino.send_command(f"LIN_MOVE:{steps}")
        self.loggers['lin'].info(f"Переход к позиции {pos_num}: {target} мм (шагов: {steps})")
        print(f"Двигаю к позиции {pos_num}: {target} мм")
    
    # ===== Управление фиксацией =====
    
    def fix_forward_start(self) -> None:
        self.loggers['fix'].info("Нажата кнопка ЗАЖАТЬ (фиксация)")
        self.arduino.send_command("FIX_FORWARD_START")
    
    def fix_back_start(self) -> None:
        self.loggers['fix'].info("Нажата кнопка РАЗЖАТЬ (фиксация)")
        self.arduino.send_command("FIX_BACK_START")
    
    def fix_stop(self) -> None:
        self.loggers['fix'].info("Остановка фиксации")
        self.arduino.send_command("FIX_STOP")
    
    def fix_move_degrees(self, degrees: float) -> None:
        """Поворот фиксации на заданное количество градусов (отрицательное = назад)"""
        # Для твоего драйвера (микрошаги 1/8)
        # 200 шагов/оборот * 8 = 1600 шагов/оборот двигателя
        # Передаточное число: 48/20 = 2.4
        # 1600 * 2.4 = 3840 шагов на 1 оборот патрона
        # 3840 / 360 = 10.666 шага на 1 градус
        STEPS_PER_DEGREE = 10.666
        steps = int(degrees * STEPS_PER_DEGREE)
        
        if steps > 0:
            self.arduino.send_command(f"FIX_MOVE:{steps}")
            self.loggers['fix'].info(f"Поворот на {degrees}° вперед ({steps} шагов)")
        elif steps < 0:
            self.arduino.send_command(f"FIX_MOVE:{steps}")
            self.loggers['fix'].info(f"Поворот на {abs(degrees)}° назад ({abs(steps)} шагов)")
        else:
            return
    
    def fix_back_exact(self) -> None:
        """Точный поворот назад на заданное количество градусов"""
        try:
            deg = self.ui.exFixPos.value()
            if deg > 0:
                self.fix_move_degrees(-deg)
                self.ui.exFixPos.setValue(0)
        except ValueError:
            self.loggers['fix'].error("Ошибка точного поворота назад")
    
    def fix_forward_exact(self) -> None:
        """Точный поворот вперед на заданное количество градусов"""
        try:
            deg = self.ui.exFixPos.value()
            if deg > 0:
                self.fix_move_degrees(deg)
                self.ui.exFixPos.setValue(0)
        except ValueError:
            self.loggers['fix'].error("Ошибка точного поворота вперед")
    
    def fix_home(self) -> None:
        self.loggers['fix'].info("Запуск поиска дома (фиксация)")
        self.show_homing_dialog("Поиск дома фиксации...")
        self.arduino.send_command("FIX_HOME_START")
        print("Поиск дома фиксации...")
    
    # ===== Управление предобжимом =====
    
    def pre_up_start(self) -> None:
        self.loggers['pre'].info("Нажата кнопка ВВЕРХ (предобжим)")
        self.arduino.send_command("PRE_UP_START")
    
    def pre_down_start(self) -> None:
        self.loggers['pre'].info("Нажата кнопка ВНИЗ (предобжим)")
        self.arduino.send_command("PRE_DOWN_START")
    
    def pre_stop(self) -> None:
        self.loggers['pre'].info("Остановка предобжима")
        self.arduino.send_command("PRE_STOP")
    
    def pre_home(self) -> None:
        self.loggers['pre'].info("Запуск поиска дома (предобжим)")
        self.show_homing_dialog("Поиск дома предобжима...")
        self.arduino.send_command("PRE_HOME_START")
        print("Поиск дома предобжима...")
    
    def pre_reset_position(self) -> None:
        self.loggers['pre'].info("Сброс позиции предобжима в 0")
        self.ui.lblPrePos.setText("0 мм")
        self.ui.lblPrePosMan.setText("0 мм")
        self.config.set("pre_position", 0)
        print("Позиция предобжима сброшена в 0")
    
    def pre_move_steps(self, mm: float) -> None:
        """Перемещение предобжима на заданное расстояние"""
        steps = int(mm * 200)
        direction = "вверх" if steps > 0 else "вниз"
        self.arduino.send_command(f"PRE_MOVE:{-steps}")
        self.loggers['pre'].info(f"Перемещение {direction} на {abs(mm)} мм ({abs(steps)} шагов)")
    
    def pre_down_exact(self) -> None:
        """Точное перемещение вниз"""
        try:
            mm = self.ui.exPrePos.value()
            if mm > 0:
                steps = int(mm * 200)
                self.arduino.send_command(f"PRE_MOVE:{steps}")
                self.loggers['pre'].info(f"Точное перемещение вниз: {mm} мм ({steps} шагов)")
                self.ui.exPrePos.setValue(0)
        except ValueError:
            self.loggers['pre'].error("Ошибка точного перемещения вниз")

    def pre_up_exact(self) -> None:
        """Точное перемещение вверх"""
        try:
            mm = self.ui.exPrePos.value()
            if mm > 0:
                steps = int(mm * 200)
                self.arduino.send_command(f"PRE_MOVE:{-steps}")
                self.loggers['pre'].info(f"Точное перемещение вверх: {mm} мм ({steps} шагов)")
                self.ui.exPrePos.setValue(0)
        except ValueError:
            self.loggers['pre'].error("Ошибка точного перемещения вверх")
    
    # ===== Управление постобжимом =====
    
    def post_forward_start(self) -> None:
        self.loggers['post'].info("Нажата кнопка ЗАКРУТИТЬ (постобжим)")
        self.arduino.send_command("POST_FORWARD_START")
    
    def post_back_start(self) -> None:
        self.loggers['post'].info("Нажата кнопка РАСКРУТИТЬ (постобжим)")
        self.arduino.send_command("POST_BACK_START")
    
    def post_stop(self) -> None:
        self.loggers['post'].info("Остановка постобжима")
        self.arduino.send_command("POST_STOP")
    
    def post_home(self) -> None:
        self.loggers['post'].info("Запуск поиска дома (постобжим)")
        self.show_homing_dialog("Поиск дома постобжима...")
        self.arduino.send_command("POST_HOME_START")
        print("Поиск дома постобжима...")
    
    # ===== Закрытие приложения =====
    
    def closeEvent(self, event) -> None:
        """Обработка закрытия окна"""
        self.hide_keyboard()
        self._is_closing = True
        
        dialog = PasswordDialog(self)
        if dialog.exec() == PasswordDialog.Accepted:
            self.fan.cleanup()  # Очищаем GPIO куллера
            self._close_homing_dialog()
            self.arduino.send_command("EMERGENCY_STOP")
            self.arduino.disconnect()
            event.accept()
        else:
            self._is_closing = False
            event.ignore()


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()