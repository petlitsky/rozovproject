from PySide6.QtCore import QObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.main_window import MainWindow


class ManualControls(QObject):
    """Управление кнопками ручного режима"""
    
    def __init__(self, main_window: 'MainWindow'):
        super().__init__()
        self.main = main_window
        self.ui = main_window.ui
        self._setup_connections()
    
    def _setup_connections(self) -> None:
        """Подключение всех кнопок"""
        # Линейное перемещение
        self._connect_linear_buttons()
        
        # Фиксация
        self._connect_fixation_buttons()
        
        # Предобжим
        self._connect_pre_crimp_buttons()
        
        # Постобжим
        self._connect_post_crimp_buttons()
        
        # Ползунки скорости
        self._connect_speed_sliders()
    
    def _connect_linear_buttons(self) -> None:
        """Подключение кнопок линейного перемещения"""
        buttons = [
            (self.ui.btnLinForward, self.main.lin_forward_start, self.main.lin_stop),
            (self.ui.btnLinBack, self.main.lin_back_start, self.main.lin_stop),
            (self.ui.btnLinForwardMan, self.main.lin_forward_start, self.main.lin_stop),
            (self.ui.btnLinBackMan, self.main.lin_back_start, self.main.lin_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        # Кнопки "Домой"
        self.ui.btnLinHome.clicked.connect(self.main.lin_home)
        self.ui.btnLinHomeMan.clicked.connect(self.main.lin_home)
        
        # Точное перемещение
        self.ui.btnLinBackEx.clicked.connect(self.main.lin_back_exact)
        self.ui.btnLinForwardEx.clicked.connect(self.main.lin_forward_exact)
        
        # Перемещение на фиксированное расстояние
        self.ui.btnBackLin1mm.clicked.connect(lambda: self.main.lin_move_steps(-1))
        self.ui.btnBackLin5mm.clicked.connect(lambda: self.main.lin_move_steps(-5))
        self.ui.btnForwardLin1mm.clicked.connect(lambda: self.main.lin_move_steps(1))
        self.ui.btnForwardLin5mm.clicked.connect(lambda: self.main.lin_move_steps(5))
        
        # Сохранение и переход к позициям
        self.ui.btnSaveLinPos1.clicked.connect(self.main.save_lin_position_1)
        self.ui.btnSaveLinPos2.clicked.connect(self.main.save_lin_position_2)
        self.ui.btnGoLinPos1.clicked.connect(lambda: self.main.go_to_lin_position(1))
        self.ui.btnGoLinPos2.clicked.connect(lambda: self.main.go_to_lin_position(2))
        self.ui.btnGoLinPos1Man.clicked.connect(lambda: self.main.go_to_lin_position(1))
        self.ui.btnGoLinPos2Man.clicked.connect(lambda: self.main.go_to_lin_position(2))
        
        # Сброс позиции
        self.ui.btnResLinPos.clicked.connect(self.main.lin_reset_position)
    
    def _connect_fixation_buttons(self) -> None:
        """Подключение кнопок фиксации"""
        buttons = [
            (self.ui.btnFixBack, self.main.fix_back_start, self.main.fix_stop),
            (self.ui.btnFixForward, self.main.fix_forward_start, self.main.fix_stop),
            (self.ui.btnFixBackMan, self.main.fix_back_start, self.main.fix_stop),
            (self.ui.btnFixForwardMan, self.main.fix_forward_start, self.main.fix_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        self.ui.btnFixHome.clicked.connect(self.main.fix_home)
    
    def _connect_pre_crimp_buttons(self) -> None:
        """Подключение кнопок предобжима"""
        buttons = [
            (self.ui.btnPreUp, self.main.pre_up_start, self.main.pre_stop),
            (self.ui.btnDownBack, self.main.pre_down_start, self.main.pre_stop),
            (self.ui.btnPreUpMan, self.main.pre_up_start, self.main.pre_stop),
            (self.ui.btnPreDownMan, self.main.pre_down_start, self.main.pre_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
        
        # Точное перемещение
        self.ui.btnUpPre5mm.clicked.connect(lambda: self.main.pre_move_steps(5))
        self.ui.btnUpPre1mm.clicked.connect(lambda: self.main.pre_move_steps(1))
        self.ui.btnDownPre1mm.clicked.connect(lambda: self.main.pre_move_steps(-1))
        self.ui.btnDownPre5mm.clicked.connect(lambda: self.main.pre_move_steps(-5))
        self.ui.btnPreDownEx.clicked.connect(self.main.pre_down_exact)
        self.ui.btnPreUpEx.clicked.connect(self.main.pre_up_exact)
        
        # Домой и сброс
        self.ui.btnPreHome.clicked.connect(self.main.pre_home)
        self.ui.btnPreHomeMan.clicked.connect(self.main.pre_home)
        self.ui.btnResPrePos.clicked.connect(self.main.pre_reset_position)
    
    def _connect_post_crimp_buttons(self) -> None:
        """Подключение кнопок постобжима"""
        buttons = [
            (self.ui.btnPostBackMan, self.main.post_back_start, self.main.post_stop),
            (self.ui.btnPostForwardMan, self.main.post_forward_start, self.main.post_stop),
        ]
        
        for btn, press, release in buttons:
            btn.pressed.connect(press)
            btn.released.connect(release)
    
    def _connect_speed_sliders(self) -> None:
        """Подключение ползунков скорости"""
        # Линейная скорость
        self.ui.linSpeed.valueChanged.connect(self._on_lin_speed_preview)
        self.ui.btnSetLinSpeed.clicked.connect(self._on_lin_speed_apply)
        
        # Скорость фиксации
        self.ui.fixSpeed.valueChanged.connect(self._on_fix_speed_preview)
        self.ui.btnSetFixSpeed.clicked.connect(self._on_fix_speed_apply)
        
        # Скорость предобжима
        self.ui.preSpeed.valueChanged.connect(self._on_pre_speed_preview)
        self.ui.btnSetPreSpeed.clicked.connect(self._on_pre_speed_apply)
        
        # Скорость постобжима
        self.ui.postSpeed.valueChanged.connect(self._on_post_speed_preview)
        self.ui.btnSetPostSpeed.clicked.connect(self._on_post_speed_apply)
    
    def _on_lin_speed_preview(self, value: int) -> None:
        self.ui.lblLinSpeed.setText(f"Скорость перемещения: {value}%")
    
    def _on_lin_speed_apply(self) -> None:
        value = self.ui.linSpeed.value()
        self.main.set_lin_speed(value)
    
    def _on_fix_speed_preview(self, value: int) -> None:
        self.ui.lblFixSpeed.setText(f"Скорость зажатия: {value}%")
    
    def _on_fix_speed_apply(self) -> None:
        value = self.ui.fixSpeed.value()
        self.main.set_fix_speed(value)
    
    def _on_pre_speed_preview(self, value: int) -> None:
        self.ui.lblPreSpeed.setText(f"Скорость перемещения: {value}%")
    
    def _on_pre_speed_apply(self) -> None:
        value = self.ui.preSpeed.value()
        self.main.set_pre_speed(value)
    
    def _on_post_speed_preview(self, value: int) -> None:
        self.ui.lblPostSpeed.setText(f"Скорость зажатия: {value}%")
    
    def _on_post_speed_apply(self) -> None:
        value = self.ui.postSpeed.value()
        self.main.set_post_speed(value)