from PySide6.QtCore import QObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class ManualControls(QObject):
    def __init__(self, main_window: 'MainWindow'):
        super().__init__()
        self.main = main_window
        self.ui = main_window.ui
        self._setup_connections()
    
    def _setup_connections(self) -> None:
        self._connect_linear_buttons()
        self._connect_fixation_buttons()
        self._connect_pre_crimp_buttons()
        self._connect_post_crimp_buttons()
        self._connect_speed_sliders()
        self._connect_fan_radio()
    
    def _connect_linear_buttons(self) -> None:
        buttons = [
            (self.ui.btnLinForward, self.main.lin_forward_start, self.main.lin_stop),
            (self.ui.btnLinBack, self.main.lin_back_start, self.main.lin_stop),
            (self.ui.btnLinForwardMan, self.main.lin_forward_start, self.main.lin_stop),
            (self.ui.btnLinBackMan, self.main.lin_back_start, self.main.lin_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        self.ui.btnLinHome.clicked.connect(self.main.lin_home)
        self.ui.btnLinHomeMan.clicked.connect(self.main.lin_home)
                
        self.ui.btnBackLin1mm.clicked.connect(lambda: self.main.lin_move_steps(-1))
        self.ui.btnBackLin5mm.clicked.connect(lambda: self.main.lin_move_steps(-5))
        self.ui.btnForwardLin1mm.clicked.connect(lambda: self.main.lin_move_steps(1))
        self.ui.btnForwardLin5mm.clicked.connect(lambda: self.main.lin_move_steps(5))
        
        self.ui.btnSaveLinPos1.clicked.connect(self.main.save_lin_position_1)
        self.ui.btnSaveLinPos2.clicked.connect(self.main.save_lin_position_2)
        self.ui.btnGoLinPos1.clicked.connect(lambda: self.main.go_to_lin_position(1))
        self.ui.btnGoLinPos2.clicked.connect(lambda: self.main.go_to_lin_position(2))
        self.ui.btnGoLinPos1Man.clicked.connect(lambda: self.main.go_to_lin_position(1))
        self.ui.btnGoLinPos2Man.clicked.connect(lambda: self.main.go_to_lin_position(2))
        
        self.ui.btnResLinPos.clicked.connect(self.main.lin_reset_position)
    
    def _connect_fixation_buttons(self) -> None:
        buttons = [
            (self.ui.btnFixBack, self.main.fix_back_start, self.main.fix_stop),
            (self.ui.btnFixForward, self.main.fix_forward_start, self.main.fix_stop),
            (self.ui.btnFixBackMan, self.main.fix_back_start, self.main.fix_stop),
            (self.ui.btnFixForwardMan, self.main.fix_forward_start, self.main.fix_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        self.ui.btnBackFix1grad.clicked.connect(lambda: self.main.fix_move_degrees(-1))
        self.ui.btnForwardFix1grad.clicked.connect(lambda: self.main.fix_move_degrees(1))
        self.ui.btnBackFix5grad.clicked.connect(lambda: self.main.fix_move_degrees(-5))
        self.ui.btnForwardFix5grad.clicked.connect(lambda: self.main.fix_move_degrees(5))
        
        self.ui.btnFixHome.clicked.connect(self.main.fix_home)
    
    def _connect_pre_crimp_buttons(self) -> None:
        buttons = [
            (self.ui.btnPreUp, self.main.pre_up_start, self.main.pre_stop),
            (self.ui.btnDownBack, self.main.pre_down_start, self.main.pre_stop),
            (self.ui.btnPreUpMan, self.main.pre_up_start, self.main.pre_stop),
            (self.ui.btnPreDownMan, self.main.pre_down_start, self.main.pre_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        self.ui.btnUpPre5mm.clicked.connect(lambda: self.main.pre_move_steps(-5))
        self.ui.btnUpPre1mm.clicked.connect(lambda: self.main.pre_move_steps(-1))
        self.ui.btnDownPre1mm.clicked.connect(lambda: self.main.pre_move_steps(1))
        self.ui.btnDownPre5mm.clicked.connect(lambda: self.main.pre_move_steps(5))
                
        self.ui.btnPreHome.clicked.connect(self.main.pre_home)
        self.ui.btnPreHomeMan.clicked.connect(self.main.pre_home)
        self.ui.btnResPrePos.clicked.connect(self.main.pre_reset_position)

        self.ui.btnSavPreForce.clicked.connect(self.main.save_pre_force)
        self.ui.btnGoPreForce.clicked.connect(self.main.go_to_pre_force)
        self.ui.btnGoPreForceMan.clicked.connect(self.main.go_to_pre_force)
    
    def _connect_post_crimp_buttons(self) -> None:
        buttons = [
            (self.ui.btnPostBack, self.main.post_back_start, self.main.post_stop),
            (self.ui.btnPostForward, self.main.post_forward_start, self.main.post_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        buttons_man = [
            (self.ui.btnPostBackMan, self.main.post_back_start, self.main.post_stop),
            (self.ui.btnPostForwardMan, self.main.post_forward_start, self.main.post_stop),
        ]
        
        for btn, press, release in buttons_man:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        self.ui.btnBackPost1grad.clicked.connect(lambda: self.main.post_move_degrees(-1))
        self.ui.btnForwardPost1grad.clicked.connect(lambda: self.main.post_move_degrees(1))
        self.ui.btnBackPost5grad.clicked.connect(lambda: self.main.post_move_degrees(-5))
        self.ui.btnForwardPost5grad.clicked.connect(lambda: self.main.post_move_degrees(5))

        self.ui.btnPostHome.clicked.connect(self.main.post_home)
    
    def _connect_speed_sliders(self) -> None:
        self.ui.linSpeed.valueChanged.connect(self._on_lin_speed_changed)
        self.ui.fixSpeed.valueChanged.connect(self._on_fix_speed_changed)
        self.ui.preSpeed.valueChanged.connect(self._on_pre_speed_changed)
        self.ui.postSpeed.valueChanged.connect(self._on_post_speed_changed)
        self.ui.fanSpeed.valueChanged.connect(self._on_fan_speed_changed)
    
    def _on_lin_speed_changed(self, value: int) -> None:
        self.ui.lblLinSpeed.setText(f"Скорость перемещения: {value}%")
        self.main.set_lin_speed(value)
     
    def _on_fix_speed_changed(self, value: int) -> None:
        self.ui.lblFixSpeed.setText(f"Скорость фиксации: {value}%")
        self.main.set_fix_speed(value)
    
    def _on_pre_speed_changed(self, value: int) -> None:
        self.ui.lblPreSpeed.setText(f"Скорость перемещения: {value}%")
        self.main.set_pre_speed(value)
    
    def _on_post_speed_changed(self, value: int) -> None:
        self.ui.lblPostSpeed.setText(f"Скорость обжима: {value}%")
        self.main.set_post_speed(value)
    
    def _on_fan_speed_changed(self, value: int) -> None:
        self.ui.lblFanSpeed.setText(f"{value}%")
        self.main.set_fan_speed(value)

    def _connect_fan_radio(self) -> None:
        self.ui.getAutoFan.clicked.connect(self.main._process_auto_fan)
        self.ui.getManualFan.clicked.connect(self.main._on_manual_fan_slider_changed)
        self.ui.fanOff.clicked.connect(self.main._set_fan_off)