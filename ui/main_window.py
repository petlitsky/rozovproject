import sys
from datetime import datetime
from typing import Optional
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QSize
from main_ui import Ui_MainWindow
from ui.dialogs import PasswordDialog, HomingDialog, ErrorDialog, show_error
from ui.graph_widget import GraphWidget
from controllers.arduino_controller import ArduinoController
from controllers.manual_controls import ManualControls
from models.config import Config
from sensors.bme280_sensor import BME280Sensor
from sensors.fan_controller import FanController
from sensors.force_sensor import ForceSensorWorker
from sensors.torque_sensor import TorqueSensorWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.showFullScreen()
        
        self.config = Config()
        self.arduino = ArduinoController(self)
        self.bme280 = BME280Sensor(self)
        self.fan = FanController(self)
        self.manual = ManualControls(self)
        
        # Состояние
        self.homing_dialog: Optional[HomingDialog] = None
        self.animation: Optional[QPropertyAnimation] = None
        self.disconnect_shown = False
        self._is_closing = False
        
        # Время старта программы
        self.start_time = datetime.now()
                
        self._setup_ui()
        self._setup_connections()
        self._setup_timer()
        self._load_saved_values()
        self._setup_graphs()

        self.force_sensor = ForceSensorWorker(dout_pin=24, pd_sck_pin=25)
        self.force_sensor.force_updated.connect(self._update_force_labels)
        self.force_sensor.start()
        self.is_moving_to_force = False
        self.pre_slowed_force = False

        self.torque_worker = TorqueSensorWorker(dout_pin=18, pd_sck_pin=23)
        self.torque_worker.torque_updated.connect(self._update_torque_labels)
        self.torque_worker.start()
        
        QTimer.singleShot(500, self._connect_arduino)
        QTimer.singleShot(3000, self._send_saved_values)
        self._update_page_values()
    
    def _setup_ui(self) -> None:
        main_buttons = [
            self.ui.btnAutoMode,
            self.ui.btnManualMode,
            self.ui.btnCalibration,
            self.ui.btnDebug,
            self.ui.btnSettings
        ]

        for btn in main_buttons:
            btn.setCheckable(True)
        
        sub_buttons = [
            self.ui.btnLinear,
            self.ui.btnFixation,
            self.ui.btnPreCrimp,
            self.ui.btnPostCrimp
        ]

        for btn in sub_buttons:
            btn.setCheckable(True)
        
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.btnManualMode.setChecked(True)
        self.ui.subMenu.setVisible(True)
        self.ui.subMenu.setMaximumSize(QSize(16777215, 189))
        
        # Настройка вентилятора - по умолчанию Auto
        self.ui.getAutoFan.setChecked(True)
        self.ui.getManualFan.setChecked(False)
        self.ui.fanOff.setChecked(False)
        self.ui.fanSpeed.setEnabled(False)

        temp_min = self.config.get("temp_min", 40.0)
        temp_max = self.config.get("temp_max", 70.0)
        start_speed = self.config.get("start_speed", 30)
    
        self.ui.tempMin.setValue(temp_min)
        self.ui.tempMax.setValue(temp_max)
        self.ui.startSpeed.setValue(start_speed)
    
        # Подключение сохранения при изменении
        self.ui.tempMin.valueChanged.connect(self._save_temp_settings)
        self.ui.tempMax.valueChanged.connect(self._save_temp_settings)
        self.ui.startSpeed.valueChanged.connect(self._save_temp_settings)
        
        # Кнопка сброса статистики
        self.ui.btnResetStats.clicked.connect(self._reset_stats)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
        self.setWindowFlag(Qt.WindowType.WindowFullscreenButtonHint, True)
    
    def _setup_graphs(self):
        """Инициализация графиков"""
        layout = self.ui.frameGraph.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.frameGraph)
            layout.setContentsMargins(0, 0, 0, 0)
        
        # Создаем виджет графика с поддержкой нескольких линий
        self.graph_widget = GraphWidget(self, max_points=500)  # 500 точек = 50 секунд при 10Гц
        
        # Добавляем линии для всех датчиков (без легенды)
        self.graph_widget.add_line("Момент", '#00ff88')    # Зеленый
        self.graph_widget.add_line("Усилие", '#ff8800')    # Оранжевый
        self.graph_widget.add_line("Ток", '#0088ff')       # Синий
        self.graph_widget.add_line("Температура", '#ff0088') # Розовый
        
        layout.addWidget(self.graph_widget)
        
        # Таймер для обновления данных на графике (10 Гц)
        self.graph_update_timer = QTimer()
        self.graph_update_timer.timeout.connect(self._update_graphs)
        self.graph_update_timer.start(100)  # 10 Гц
        
        # Таймер для обновления вида (скролл) - отдельно, реже
        self.view_update_timer = QTimer()
        self.view_update_timer.timeout.connect(self._update_view)
        self.view_update_timer.start(500)  # 2 Гц
        
        # Таймер для обновления текста (медленно - 1 Гц)
        self.text_update_timer = QTimer()
        self.text_update_timer.timeout.connect(self._update_text_slow)
        self.text_update_timer.start(1000)  # 1 Гц
        
        # Таймер для обновления времени работы
        self.time_timer = QTimer()
        self.time_timer.timeout.connect(self._update_time)
        self.time_timer.start(1000)  # 1 Гц
        
        # Данные для графиков
        self.torque_data = []
        self.force_data = []
        self.current_data = []
        self.temp_data = []
        
        # Флаги для сбора статистики
        self.torque_max = self.config.get("torque_max", 0.0)
        self.torque_min = self.config.get("torque_min", 0.0)
        self.torque_avg = 0.0
        self.torque_count = 0
        
        self.force_max = self.config.get("force_max", 0.0)
        self.force_min = self.config.get("force_min", 0.0)
        self.force_avg = 0.0
        self.force_count = 0
        
        self.current_max = self.config.get("current_max", 0.0)
        self.current_min = self.config.get("current_min", 0.0)
        self.current_avg = 0.0
        self.current_count = 0
        self.current_value = 0.0
        
        # Текущий режим отображения
        self.current_graph_mode = self.ui.comboBoxSensor.currentIndex()
        
        # Подключение comboBox
        self.ui.comboBoxSensor.currentIndexChanged.connect(self._on_sensor_changed)
        
        # Изначально показываем только момент (индекс 0)
        self._on_sensor_changed(0)
    
    def _setup_connections(self) -> None:
        self.ui.btnExit.clicked.connect(self.close)
        
        self.ui.btnAutoMode.clicked.connect(lambda: self._on_main_button_clicked(0))
        self.ui.btnManualMode.clicked.connect(lambda: self._on_main_button_clicked(1))
        self.ui.btnCalibration.clicked.connect(lambda: self._on_main_button_clicked(2))
        self.ui.btnDebug.clicked.connect(lambda: self._on_main_button_clicked(3))
        self.ui.btnSettings.clicked.connect(lambda: self._on_main_button_clicked(4))
        
        self.ui.btnLinear.clicked.connect(lambda: self._on_sub_button_clicked(0))
        self.ui.btnFixation.clicked.connect(lambda: self._on_sub_button_clicked(1))
        self.ui.btnPreCrimp.clicked.connect(lambda: self._on_sub_button_clicked(2))
        self.ui.btnPostCrimp.clicked.connect(lambda: self._on_sub_button_clicked(3))
        
        self.arduino.position_updated.connect(self._update_position)
        self.arduino.moving.connect(self._on_moving)
        self.arduino.home_found.connect(self._on_home_found)
        self.arduino.limit_reached.connect(self._on_limit_reached)
        self.arduino.disconnected.connect(self._handle_disconnect)
        self.arduino.current_updated.connect(self._update_current)
        
        self.bme280.temperature_updated.connect(self._update_temperature)
        
        self.fan.fan_speed_updated.connect(self._update_fan_speed)
        
        # Подключение режимов вентилятора
        self.ui.getAutoFan.clicked.connect(self._on_fan_auto)
        self.ui.getManualFan.clicked.connect(self._on_fan_manual)
        self.ui.fanOff.clicked.connect(self._on_fan_off)
        self.ui.fanSpeed.valueChanged.connect(self._on_fan_speed_slider)
    
    def _setup_timer(self) -> None:
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_datetime)
        self.timer.start(1000)
        self._update_datetime()
    
    def _update_datetime(self) -> None:
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.ui.lblDate.setText(now)
    
    def _save_temp_settings(self):
        """Сохранение настроек температуры"""
        self.config.set("temp_min", self.ui.tempMin.value())
        self.config.set("temp_max", self.ui.tempMax.value())
        self.config.set("start_speed", self.ui.startSpeed.value())

    def _update_time(self) -> None:
        """Обновление времени работы программы в lblTimeStart (только секунды)"""
        elapsed = datetime.now() - self.start_time
        total_seconds = int(elapsed.total_seconds())
        
        # Склонение слова "секунда"
        if total_seconds % 10 == 1 and total_seconds % 100 != 11:
            word = "секунда"
        elif 2 <= total_seconds % 10 <= 4 and not (12 <= total_seconds % 100 <= 14):
            word = "секунды"
        else:
            word = "секунд"
        
        self.ui.lblTimeStart.setText(f"{total_seconds} {word}")
    
    # ===== Вентилятор =====
    
    def _on_fan_auto(self):
        """Режим Auto - управление по температуре"""
        self.ui.getAutoFan.setChecked(True)
        self.ui.getManualFan.setChecked(False)
        self.ui.fanOff.setChecked(False)
        self.ui.fanSpeed.setEnabled(False)
        self._process_auto_fan()
    
    def _on_fan_manual(self):
        """Режим Manual - ручное управление"""
        self.ui.getAutoFan.setChecked(False)
        self.ui.getManualFan.setChecked(True)
        self.ui.fanOff.setChecked(False)
        self.ui.fanSpeed.setEnabled(True)
        # Применяем текущее значение слайдера
        speed = self.ui.fanSpeed.value()
        self.fan.set_speed(speed)
    
    def _on_fan_off(self):
        """Режим Off - вентилятор выключен"""
        self.ui.getAutoFan.setChecked(False)
        self.ui.getManualFan.setChecked(False)
        self.ui.fanOff.setChecked(True)
        self.ui.fanSpeed.setEnabled(False)
        self.fan.set_speed(0)
    
    def _on_fan_speed_slider(self, value: int):
        """Изменение скорости в ручном режиме"""
        if self.ui.getManualFan.isChecked():
            self.fan.set_speed(value)
            self.ui.lblFanSpeed.setText(f"{value}%")
    
    def _process_auto_fan(self) -> None:
        """Вычисление скорости вентилятора по температуре"""
        if not self.ui.getAutoFan.isChecked():
            return

        min_temp = float(self.ui.tempMin.value()) if hasattr(self.ui, 'tempMin') else 40.0
        max_temp = float(self.ui.tempMax.value()) if hasattr(self.ui, 'tempMax') else 70.0
        start_speed = int(self.ui.startSpeed.value()) if hasattr(self.ui, 'startSpeed') else 30

        current_temp = self.bme280.get_temperature()

        if current_temp <= min_temp:
            target_speed = 0
        elif current_temp >= max_temp:
            target_speed = 100
        else:
            temp_range = max_temp - min_temp
            if temp_range > 0:
                progress = (current_temp - min_temp) / temp_range
                target_speed = int(start_speed + progress * (100 - start_speed))
            else:
                target_speed = start_speed

        self.fan.set_speed(target_speed)
    
    def _update_fan_speed(self, speed: int) -> None:
        """Обновление отображения скорости вентилятора"""
        self.ui.lblFanSpeed.setText(f"{speed}%")
        if not self.ui.getManualFan.isChecked() and not self.ui.fanOff.isChecked():
            # В режиме Auto обновляем слайдер для отображения
            self.ui.fanSpeed.setValue(speed)
    
    # ===== Датчики =====
    
    def _update_current(self, value: float):
        """Обновление тока с ACS712"""
        self.current_value = value
        # Сохраняем данные для графика
        self.current_data.append(value)
        if len(self.current_data) > 500:
            self.current_data.pop(0)
        
        # Добавляем данные в график (всегда)
        self.graph_widget.add_data_point("Ток", value)
        
        # Обновляем lblFixCur
        self.ui.lblFixCur.setText(f"{value:.2f} А")
        
        # Обновляем статистику
        self.current_count += 1
        if value > self.current_max:
            self.current_max = value
            self.config.set("current_max", value)
        if value < self.current_min or self.current_count == 1:
            self.current_min = value
            self.config.set("current_min", value)
        self.current_avg = ((self.current_avg * (self.current_count - 1)) + value) / self.current_count
            
    def _update_force_labels(self, value: float):
        if self.is_moving_to_force:
            target = float(self.config.get("target_pre_force", 0.0))

            current_pos = self.config.get("pre_position", 0)
            if current_pos >= 40 and not self.pre_slowed_force:
                self.pre_slowed_force = True
                self.arduino.send_command("PRE_SPEED:5")
                self.arduino.send_command("PRE_DOWN_START")

            if (target > 50 and value - 15 >= target) or (target > 40 and value - 10 >= target) or value >= target:
                self.arduino.send_command("PRE_STOP")
                self.is_moving_to_force = False
                self.pre_slowed_force = False
                speed = self.config.get("pre_speed", 30)
                self.arduino.send_command(f"PRE_SPEED:{speed}")

        if value < 0.5 : value = 0
        self.ui.lblPreForceMan.setText(f"{value:.1f} Н")
        self.ui.lblPreForce.setText(f"{value:.1f} Н")
        
        # Сохраняем данные для графика
        self.force_data.append(value)
        if len(self.force_data) > 500:
            self.force_data.pop(0)
        
        # Обновляем статистику
        self.force_count += 1
        if value > self.force_max:
            self.force_max = value
            self.config.set("force_max", value)
        if value < self.force_min or self.force_count == 1:
            self.force_min = value
            self.config.set("force_min", value)
        self.force_avg = ((self.force_avg * (self.force_count - 1)) + value) / self.force_count
        
        # Добавляем данные в график
        self.graph_widget.add_data_point("Усилие", value)
    
    def _update_torque_labels(self, value: float):
        self.ui.lblPostTorqMan.setText(f"{value:.3f} Н·м")
        self.ui.lblPostTorq.setText(f"{value:.3f} Н·м")
        
        # Сохраняем данные для графика
        self.torque_data.append(value)
        if len(self.torque_data) > 500:
            self.torque_data.pop(0)
        
        # Обновляем статистику
        self.torque_count += 1
        if value > self.torque_max:
            self.torque_max = value
            self.config.set("torque_max", value)
        if value < self.torque_min or self.torque_count == 1:
            self.torque_min = value
            self.config.set("torque_min", value)
        self.torque_avg = ((self.torque_avg * (self.torque_count - 1)) + value) / self.torque_count
        
        # Добавляем данные в график
        self.graph_widget.add_data_point("Момент", value)
    
    def _update_temperature(self, temp: float) -> None:
        self.ui.lblTemp.setText(f"Температура: {temp:.1f}°C")
        
        # Сохраняем данные для графика
        self.temp_data.append(temp)
        if len(self.temp_data) > 500:
            self.temp_data.pop(0)
        
        # Добавляем данные в график
        self.graph_widget.add_data_point("Температура", temp)
        
        # В режиме Auto - обновляем скорость вентилятора
        if self.ui.getAutoFan.isChecked():
            self._process_auto_fan()
    
    # ===== Сброс статистики =====
    
    def _reset_stats(self):
        """Сброс максимальных и минимальных значений"""
        # Сбрасываем момент
        self.torque_max = 0.0
        self.torque_min = 0.0
        self.torque_avg = 0.0
        self.torque_count = 0
        self.config.set("torque_max", 0.0)
        self.config.set("torque_min", 0.0)
        
        # Сбрасываем усилие
        self.force_max = 0.0
        self.force_min = 0.0
        self.force_avg = 0.0
        self.force_count = 0
        self.config.set("force_max", 0.0)
        self.config.set("force_min", 0.0)
        
        # Сбрасываем ток
        self.current_max = 0.0
        self.current_min = 0.0
        self.current_avg = 0.0
        self.current_count = 0
        self.config.set("current_max", 0.0)
        self.config.set("current_min", 0.0)
        
        # Обновляем отображение
        self._update_text_slow()
    
    # ===== Остальные методы =====
    
    def _load_saved_values(self) -> None:
        speeds = [
            ('lin_speed', self.ui.linSpeed, self.ui.lblLinSpeed, "Скорость перемещения: {}%"),
            ('fix_speed', self.ui.fixSpeed, self.ui.lblFixSpeed, "Скорость зажатия: {}%"),
            ('pre_speed', self.ui.preSpeed, self.ui.lblPreSpeed, "Скорость перемещения: {}%"),
            ('post_speed', self.ui.postSpeed, self.ui.lblPostSpeed, "Скорость зажатия: {}%"),
        ]

        positions = [
            ('lin_position', self.ui.lblLinPos, self.ui.lblLinPosMan, "{} мм"),
            ('pre_position', self.ui.lblPrePos, self.ui.lblPrePosMan, "{} мм"),
        ]

        savepos = [
            ('lin_pos1', self.ui.lblPosLinPre, "Текущая позиция предобжима: {} мм"),
            ('lin_pos2', self.ui.lblPosLinPost, "Текущая позиция постобжима: {} мм"),
            ('target_pre_force', self.ui.lblSaveForcePre, "Текущее сохраненное усилие: {} Н"),
        ]
        
        for key, slider, label, template in speeds:
            value = self.config.get(key, 30)
            slider.setValue(value)
            label.setText(template.format(value))

        for key, label, labelMan, template in positions:
            value = self.config.get(key, 0)
            labelMan.setText(template.format(value))
            label.setText(template.format(value))

        for key, label, template in savepos:
            value = self.config.get(key, 0)
            label.setText(template.format(value))
        
        fan_value = self.config.get('fan_speed', 50)
        self.ui.fanSpeed.setValue(fan_value)
        self.ui.lblFanSpeed.setText(f"{fan_value}%")
    
    def _connect_arduino(self) -> None:
        if not self.arduino.connect():
            show_error(self, "Ошибка подключения", "Arduino не найдена!\nПроверьте подключение и порт.")
            return

    def _send_saved_values(self):
        if not self.arduino.is_connected:
            return

        lin_speed = self.config.get("lin_speed", 50)
        fix_speed = self.config.get("fix_speed", 30)
        pre_speed = self.config.get("pre_speed", 30)
        post_speed = self.config.get("post_speed", 30)
        lin_position = self.config.get("lin_position", 0)
        pre_position = self.config.get("pre_position", 0)

        commands = [
            f"LIN_SPEED:{lin_speed}",
            f"FIX_SPEED:{fix_speed}",
            f"PRE_SPEED:{pre_speed}",
            f"POST_SPEED:{post_speed}",
            f"LIN_SET_POS:{lin_position}",
            f"PRE_SET_POS:{pre_position}",
        ]

        for cmd in commands:
            self.arduino.send_command(cmd)
        
    def _on_main_button_clicked(self, index: int) -> None:
        self._clear_all_selection()
        
        buttons = [
            self.ui.btnAutoMode,
            self.ui.btnManualMode,
            self.ui.btnCalibration,
            self.ui.btnDebug,
            self.ui.btnSettings
        ]
        
        if index == 1:
            self._toggle_submenu(True)
        else:
            self._toggle_submenu(False)
        
        buttons[index].setChecked(True)
        self._switch_page(index)
    
    def _on_sub_button_clicked(self, index: int) -> None:
        sub_buttons = [self.ui.btnLinear, self.ui.btnFixation, self.ui.btnPreCrimp, self.ui.btnPostCrimp]

        for btn in sub_buttons:
            btn.setChecked(False)
        
        sub_buttons[index].setChecked(True)
        
        self.ui.btnManualMode.setChecked(True)
        self._switch_page(5 + index)
    
    def _clear_all_selection(self) -> None:
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
        if self.animation:
            self.animation.stop()
            self.animation = None
        
        if show:
            self.ui.subMenu.setVisible(True)
            self.animation = QPropertyAnimation(self.ui.subMenu, b"maximumSize")
            self.animation.setDuration(200)
            self.animation.setEasingCurve(QEasingCurve.Type.OutQuad)
            self.animation.setEndValue(QSize(16777215, 189))
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
        self.ui.stackedWidget.setCurrentIndex(index)
        self._update_page_values()
    
    def _update_page_values(self) -> None:
        if self.arduino.is_connected:
            self.arduino.send_command("GET_POS")
    
    # ===== Обработчики сигналов Arduino =====
    
    def _update_position(self, axis: str, position: int) -> None:
        if axis == "LIN":
            self.ui.lblLinPos.setText(f"{position} мм")
            self.ui.lblLinPosMan.setText(f"{position} мм")
            self.config.set("lin_position", position)
        elif axis == "PRE":
            self.ui.lblPrePos.setText(f"{position} мм")
            self.ui.lblPrePosMan.setText(f"{position} мм")
            self.config.set("pre_position", position)
    
    def _on_moving(self, axis: str) -> None:
        if axis == "LIN":
            self.ui.lblLinPos.setText("MOVING...")
            self.ui.lblLinPosMan.setText("MOVING...")
        elif axis == "PRE":
            self.ui.lblPrePos.setText("MOVING...")
            self.ui.lblPrePosMan.setText("MOVING...")
    
    def _on_home_found(self, axis: str) -> None:
        messages = {
            "LIN": ("Дом линейного перемещения найден!", "lin"),
            "PRE": ("Дом предобжима найден!", "pre"),
            "FIX": ("Дом фиксации найден!", "fix"),
            "POST": ("Дом постобжима найден!", "post"),
        }
        
        if axis in messages:
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
        messages = {
            ("LIN", "BACK"): ("Достигнут концевик НАЗАД", "lin"),
            ("LIN", "FORWARD"): ("Достигнут концевик ВПЕРЕД", "lin"),
            ("PRE", "UP"): ("Достигнут концевик предобжима ВВЕРХ", "pre"),
            ("PRE", "DOWN"): ("Достигнут концевик предобжима ВНИЗ", "pre"),
        }
        
        if (axis, direction) in messages:
            self._close_homing_dialog()
    
    def _handle_disconnect(self) -> None:
        if self._is_closing:
            return
        
        if self.disconnect_shown:
            return
        
        self.disconnect_shown = True
        self._close_homing_dialog()
                
        show_error(self, "Потеря соединения", "Arduino отключена!\nПроверьте подключение.")
    
    # ===== Утилиты для диалогов =====
    
    def show_homing_dialog(self, text: str) -> None:
        if not self.arduino.is_connected:
            return
        
        if self.homing_dialog is None or not self.homing_dialog.isVisible():
            self.homing_dialog = HomingDialog(self, text)
            self.homing_dialog.show()
    
    def _close_homing_dialog(self) -> None:
        if self.homing_dialog and self.homing_dialog.isVisible():
            self.homing_dialog.accept()
            self.homing_dialog = None
        
    def set_lin_speed(self, value: int) -> None:
        self.config.set("lin_speed", value)
        self.arduino.send_command(f"LIN_SPEED:{value}")
    
    def set_fix_speed(self, value: int) -> None:
        self.config.set("fix_speed", value)
        self.arduino.send_command(f"FIX_SPEED:{value}")
    
    def set_pre_speed(self, value: int) -> None:
        self.config.set("pre_speed", value)
        self.arduino.send_command(f"PRE_SPEED:{value}")
    
    def set_post_speed(self, value: int) -> None:
        self.config.set("post_speed", value)
        self.arduino.send_command(f"POST_SPEED:{value}")
    
    def set_fan_speed(self, value: int) -> None:
        self.config.set("fan_speed", value)
        self.fan.set_speed(value)
        
    def lin_forward_start(self) -> None:
        self.arduino.send_command("LIN_FORWARD_START")
    
    def lin_back_start(self) -> None:
        self.arduino.send_command("LIN_BACK_START")
    
    def lin_stop(self) -> None:
        self.arduino.send_command("LIN_STOP")
    
    def lin_home(self) -> None:
        self.show_homing_dialog("Поиск дома линейного перемещения...")
        self.arduino.send_command("LIN_HOME_START")
    
    def lin_reset_position(self) -> None:
        self.ui.lblLinPos.setText("0 мм")
        self.ui.lblLinPosMan.setText("0 мм")
        self.config.set("lin_position", 0)
    
    def lin_move_steps(self, mm: float) -> None:
        steps = int(mm * 100)
        self.arduino.send_command(f"LIN_MOVE:{steps}")
    
    def lin_back_exact(self) -> None:
        mm = self.ui.exLinPos.value()
        if mm > 0:
            steps = int(mm * 100)
            self.arduino.send_command(f"LIN_MOVE:{-steps}")
            
    def lin_forward_exact(self) -> None:
        mm = self.ui.exLinPos.value()
        if mm > 0:
            steps = int(mm * 100)
            self.arduino.send_command(f"LIN_MOVE:{steps}")
            
    def _get_current_lin_position(self) -> int:
        text = self.ui.lblLinPos.text().replace(" мм", "").replace("MOVING...", "")
        try:
            return int(text) if text else 0
        except ValueError:
            return 0
    
    def save_lin_position_1(self) -> None:
        pos = self._get_current_lin_position()
        self.ui.lblPosLinPre.setText(f"Текущая позиция предобжима: {pos} мм")
        self.config.set("lin_pos1", pos)
    
    def save_lin_position_2(self) -> None:
        pos = self._get_current_lin_position()
        self.ui.lblPosLinPost.setText(f"Текущая позиция постобжима: {pos} мм")
        self.config.set("lin_pos2", pos)

    def go_to_lin_position(self, pos_num: int) -> None:
        target = self.config.get(f"lin_pos{pos_num}", 0)
        current = self._get_current_lin_position()
        
        diff = target - current
        if diff == 0:
            return
        
        steps = diff * 100
        self.arduino.send_command(f"LIN_MOVE:{steps}")
    
    def fix_forward_start(self) -> None:
        self.arduino.send_command("FIX_FORWARD_START")
    
    def fix_back_start(self) -> None:
        self.arduino.send_command("FIX_BACK_START")
    
    def fix_stop(self) -> None:
        self.arduino.send_command("FIX_STOP")
    
    def fix_move_degrees(self, degrees: float) -> None:
        STEPS_PER_DEGREE = 10.666
        steps = int(degrees * STEPS_PER_DEGREE)
        
        if steps > 0:
            self.arduino.send_command(f"FIX_MOVE:{steps}")
        elif steps < 0:
            self.arduino.send_command(f"FIX_MOVE:{steps}")
        else:
            return
                
    def fix_home(self) -> None:
        self.show_homing_dialog("Поиск дома фиксации...")
        self.arduino.send_command("FIX_HOME_START")
            
    def pre_up_start(self) -> None:
        self.arduino.send_command("PRE_UP_START")
    
    def pre_down_start(self) -> None:
        self.arduino.send_command("PRE_DOWN_START")
    

    def save_pre_force(self) -> None:
        force = round(self.force_sensor.get_current_force(), 1)
        self.ui.lblSaveForcePre.setText(f"Текущее сохраненное усилие: {force} Н")
        self.config.set("target_pre_force", force)

    def go_to_pre_force(self) -> None:
        target = self.config.get(f"target_pre_force", 0.0)
        current = self.force_sensor.get_current_force()
        
        
        diff = target - current
        if diff <= 0:
            return

        self.is_moving_to_force = True

        current_pos = self.config.get("pre_position", 0)
        target_pos = 40-current_pos

        if target_pos < 0 : target_pos = 0
        
        self.pre_move_steps(target_pos)

    def pre_stop(self) -> None:
        self.arduino.send_command("PRE_STOP")
    
    def pre_home(self) -> None:
        self.show_homing_dialog("Поиск дома предобжима...")
        self.arduino.send_command("PRE_HOME_START")
    
    def pre_reset_position(self) -> None:
        self.ui.lblPrePos.setText("0 мм")
        self.ui.lblPrePosMan.setText("0 мм")
        self.config.set("pre_position", 0)
    
    def pre_move_steps(self, mm: float) -> None:
        steps = int(mm * 200)
        self.arduino.send_command(f"PRE_MOVE:{steps}")
    
    def pre_down_exact(self) -> None:
        mm = self.ui.exPrePos.value()
        if mm > 0:
            steps = int(mm * 200)
            self.arduino.send_command(f"PRE_MOVE:{steps}")
        
    def pre_up_exact(self) -> None:
        mm = self.ui.exPrePos.value()
        if mm > 0:
            steps = int(mm * 200)
            self.arduino.send_command(f"PRE_MOVE:{-steps}")
        
    def post_forward_start(self) -> None:
        self.arduino.send_command("POST_FORWARD_START")
    
    def post_back_start(self) -> None:
        self.arduino.send_command("POST_BACK_START")
    
    def post_stop(self) -> None:
        self.arduino.send_command("POST_STOP")
    
    def post_home(self) -> None:
        self.show_homing_dialog("Поиск дома постобжима...")
        self.arduino.send_command("POST_HOME_START")

    def post_move_degrees(self, degrees: float) -> None:
        STEPS_PER_DEGREE = 10.666
        steps = int(degrees * STEPS_PER_DEGREE)
        
        if steps != 0:
            self.arduino.send_command(f"POST_MOVE:{-steps}")
        else:
            return
    
    # ===== Методы для графиков =====
    
    def _on_sensor_changed(self, index: int):
        """Обработка изменения выбора датчика в comboBox"""
        self.current_graph_mode = index
        
        # Очищаем lblSensData при переключении
        self.ui.lblSensData.setText("")
        
        # Показываем только выбранную линию (0-Момент, 1-Усилие, 2-Ток, 3-Температура)
        names = list(self.graph_widget.lines_data.keys())
        for i, name in enumerate(names):
            if i == index:
                self.graph_widget.lines_data[name]['line'].setVisible(True)
            else:
                self.graph_widget.lines_data[name]['line'].setVisible(False)
        
        # Обновляем статистику и текст
        self._update_text_slow()
    
    def _update_graphs(self):
        """Обновление данных на графике (10 Гц)"""
        # Данные приходят через сигналы, ничего не делаем
        pass
    
    def _update_view(self):
        """Обновление вида графика (скролл) - ограничение 50 секунд"""
        if self.graph_widget.is_auto_scroll and self.graph_widget.lines_data:
            first_line = next(iter(self.graph_widget.lines_data.values()))
            if first_line['x']:
                max_time = first_line['x'][-1]
                min_time = max(0, max_time - 50)  # Показываем последние 50 секунд
                self.graph_widget.plot_widget.setXRange(min_time, max_time, padding=0)
    
    def _update_text_slow(self):
        """Медленное обновление текста (1 Гц)"""
        mode = self.current_graph_mode
        
        if mode == 0:  # Момент
            self._update_sensor_info_torque()
        elif mode == 1:  # Усилие
            self._update_sensor_info_force()
        elif mode == 2:  # Ток
            self._update_sensor_info_current()
        elif mode == 3:  # Температура
            self._update_sensor_info_temp()
    
    def _update_sensor_info_torque(self):
        """Обновление информации о моменте"""
        if self.torque_count > 0:
            info = (
                f"Макс: {self.torque_max:.3f} Н·м | "
                f"Мин: {self.torque_min:.3f} Н·м | "
                f"Сред: {self.torque_avg:.3f} Н·м | "
                f"Текущий: {self.torque_data[-1] if self.torque_data else 0:.3f} Н·м"
            )
        else:
            info = "Нет данных по моменту"
        self.ui.lblSensData.setText(info)
    
    def _update_sensor_info_force(self):
        """Обновление информации об усилии"""
        if self.force_count > 0:
            info = (
                f"Макс: {self.force_max:.1f} Н | "
                f"Мин: {self.force_min:.1f} Н | "
                f"Сред: {self.force_avg:.1f} Н | "
                f"Текущий: {self.force_data[-1] if self.force_data else 0:.1f} Н"
            )
        else:
            info = "Нет данных по усилию"
        self.ui.lblSensData.setText(info)
    
    def _update_sensor_info_current(self):
        """Обновление информации о токе"""
        if self.current_count > 0:
            info = (
                f"Макс: {self.current_max:.2f} А | "
                f"Мин: {self.current_min:.2f} А | "
                f"Сред: {self.current_avg:.2f} А | "
                f"Текущий: {self.current_data[-1] if self.current_data else 0:.2f} А"
            )
        else:
            info = "Нет данных по току"
        self.ui.lblSensData.setText(info)
    
    def _update_sensor_info_temp(self):
        """Обновление информации о температуре"""
        if self.temp_data:
            info = f"Температура: {self.temp_data[-1]:.1f}°C"
        else:
            info = "Нет данных по температуре"
        self.ui.lblSensData.setText(info)
        
    def closeEvent(self, event) -> None:
        self._is_closing = True
        
        dialog = PasswordDialog(self)
        if dialog.exec() == PasswordDialog.Accepted:
            self.graph_update_timer.stop()
            self.view_update_timer.stop()
            self.text_update_timer.stop()
            self.time_timer.stop()
            self.fan.cleanup()
            self.force_sensor.stop()
            self.torque_worker.stop()
            self._close_homing_dialog()
            self.arduino.send_command("EMERGENCY_STOP")
            self.arduino.disconnect()
            event.accept()
        else:
            self._is_closing = False
            event.ignore()