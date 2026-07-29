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
from sensors.bme280_sensor import BME280Sensor
from sensors.fan_controller import FanController
from sensors.force_sensor import ForceSensorWorker
from sensors.torque_sensor import TorqueSensorWorker


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        #self.setFixedSize(1024,600)
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
                
        self._setup_ui()
        self._setup_connections()
        self._setup_timer()

        self._load_saved_values()

        self.force_sensor = ForceSensorWorker(dout_pin=24, pd_sck_pin=25)
        self.force_sensor.force_updated.connect(self._update_force_labels)
        self.force_sensor.start()
        self.is_moving_to_force = False

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
        
        self.bme280.temperature_updated.connect(self._update_temperature)
        
        self.fan.fan_speed_updated.connect(self._update_fan_speed)
    
    def _setup_timer(self) -> None:
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_datetime)
        self.timer.start(1000)
        self._update_datetime()
    
    def _update_datetime(self) -> None:
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.ui.lblDate.setText(now)
    
    def _update_force_labels(self, value: float):
        if self.is_moving_to_force:
            target = float(self.config.get("target_pre_force", 0.0))

            current_pos = self.config.get("pre_position", 0)
            if current_pos == 35:
                self.arduino.send_command("PRE_SET_SPEED:10")

            if value >= target:
                self.arduino.send_command("PRE_STOP")
                self.is_moving_to_force = False
                speed = self.config.get("pre_speed", 30)
                self.arduino.send_command(f"PRE_SET_SPEED:{speed}")

        self.ui.lblPreForceMan.setText(f"{value:.4f} Н")
        self.ui.lblPreForce.setText(f"{value:.4f} Н")
        
    def _update_torque_labels(self, value: float):
        self.ui.lblPostTorqMan.setText(f"{value:.3f} Н·м")
        self.ui.lblPostTorq.setText(f"{value:.3f} Н·м")

    def _update_temperature(self, temp: float) -> None:
        self.ui.lblTemp.setText(f"Температура: {temp:.1f}°C")
    
    def _update_fan_speed(self, speed: int) -> None:
        self.ui.lblFanSpeed.setText(f"{speed}%")
    
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
        
        for key, slider, label, template in speeds:
            value = self.config.get(key, 30)
            slider.setValue(value)
            label.setText(template.format(value))

        for key, label, labelMan, template in positions:
            value = self.config.get(key, 30)
            labelMan.setText(template.format(value))
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

        # 1. Читаем настройки из Config
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
        self.config.set("lin_pos1", pos)
    
    def save_lin_position_2(self) -> None:
        pos = self._get_current_lin_position()
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
    
    def fix_back_exact(self) -> None:
        deg = self.ui.exFixPos.value()
        if deg > 0:
            self.fix_move_degrees(-deg)
            
    def fix_forward_exact(self) -> None:
        deg = self.ui.exFixPos.value()
        if deg > 0:
            self.fix_move_degrees(deg)
            self.ui.exFixPos.setValue(0)
            
    def fix_home(self) -> None:
        self.show_homing_dialog("Поиск дома фиксации...")
        self.arduino.send_command("FIX_HOME_START")
            
    def pre_up_start(self) -> None:
        self.arduino.send_command("PRE_UP_START")
    
    def pre_down_start(self) -> None:
        self.arduino.send_command("PRE_DOWN_START")
    

    def save_pre_force(self) -> None:
        force = self.force_sensor.get_current_force()
        self.config.set("target_pre_force", force)
        print(f"save {force}")

    def go_to_pre_force(self) -> None:
        target = self.config.get(f"target_pre_force", 0.0)
        current = self.force_sensor.get_current_force()
        
        
        diff = target - current
        if diff <= 0:
            return

        self.is_moving_to_force = True

        current_pos = self.config.get("pre_position", 0)
        target_pos = 35-current_pos

        if target_pos < 0 : target = 0
        
        self.pre_move_steps(target)

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
            
    def closeEvent(self, event) -> None:
        self._is_closing = True
        
        dialog = PasswordDialog(self)
        if dialog.exec() == PasswordDialog.Accepted:
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