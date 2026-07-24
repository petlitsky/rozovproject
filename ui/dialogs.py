# ui/dialogs.py
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton
)
from PySide6.QtCore import Qt, QTimer
import subprocess


class BaseDialog(QDialog):
    """Базовый класс для всех диалогов"""
    
    def __init__(self, parent=None, width=300, height=150, modal=True):
        super().__init__(parent)
        
        self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
        self.setModal(modal)
        self.setFixedSize(width, height)
        
        self._setup_styles()
    
    def _setup_styles(self) -> None:
        """Настройка стилей"""
        self.setStyleSheet("""
            QDialog {
                background-color: #e9ecf1;
                border-radius: 7px;
                border: 2px solid #cdced2;
            }
            
            QLabel {
                background: transparent;
                color: #2c3e50;
            }
            
            QPushButton {
                text-align: center;
                height: 30px;
                padding: 0 20px;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
    
    def closeEvent(self, event) -> None:
        """Блокируем закрытие через крестик"""
        event.ignore()
    
    def keyPressEvent(self, event) -> None:
        """Блокируем ESC"""
        if event.key() == Qt.Key.Key_Escape:
            event.ignore()
            return
        super().keyPressEvent(event)


class PasswordDialog(BaseDialog):
    """Диалог ввода пароля"""
    
    def __init__(self, parent=None):
        super().__init__(parent, width=300, height=170)
        
        self.setWindowTitle("Введите пароль")
        
        self.keyboard_process = None
        self.keyboard_visible = False
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        label = QLabel("Введите пароль для выхода:")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-weight: bold;")
        layout.addWidget(label)
        
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setFocus()
        self.password_input.original_mouse_press = self.password_input.mousePressEvent
        self.password_input.mousePressEvent = self._on_password_field_click
        layout.addWidget(self.password_input)
        
        self.error_label = QLabel("Неверный пароль!")
        self.error_label.setStyleSheet("color: #e74c3c; font-size: 12px;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.hide()
        layout.addWidget(self.error_label)
        
        button_layout = QHBoxLayout()
        
        self.ok_button = QPushButton("OK")
        self.ok_button.setStyleSheet("background-color: #bdcfdd; border: 2px solid #a6b8c6;")
        self.ok_button.clicked.connect(self._check_password)
        self.ok_button.setDefault(True)
        
        self.cancel_button = QPushButton("Отмена")
        self.cancel_button.setStyleSheet("background-color: #d5d8df; border: 2px solid #babec7;")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)
        
        self.password_input.setFocus()
    
    def _on_password_field_click(self, event):
        self.toggle_keyboard()
        if self.password_input.original_mouse_press:
            self.password_input.original_mouse_press(event)
    
    def toggle_keyboard(self):
        if self.keyboard_visible:
            self.hide_keyboard()
        else:
            self.show_keyboard()
    
    def show_keyboard(self):
        if self.keyboard_process is None or self.keyboard_process.poll() is not None:
            try:
                self.keyboard_process = subprocess.Popen(["matchbox-keyboard", "-i", "-v"])
                self.keyboard_visible = True
            except:
                try:
                    self.keyboard_process = subprocess.Popen(["onboard", "--xid"])
                    self.keyboard_visible = True
                except:
                    pass
    
    def hide_keyboard(self):
        if self.keyboard_process and self.keyboard_process.poll() is None:
            self.keyboard_process.terminate()
            self.keyboard_process = None
            self.keyboard_visible = False
    
    def _check_password(self):
        if self.password_input.text() == "1111":
            self.hide_keyboard()
            self.accept()
        else:
            self.error_label.show()
            self.password_input.setStyleSheet("""
                QLineEdit {
                    border: 1px solid #e74c3c;
                    background-color: #fff5f5;
                    padding: 5px;
                    border-radius: 5px;
                }
            """)
            self.password_input.clear()
            self.password_input.setFocus()
    
    def closeEvent(self, event):
        self.hide_keyboard()
        event.ignore()
    
    def done(self, result):
        self.hide_keyboard()
        super().done(result)


class HomingDialog(BaseDialog):
    """Диалог поиска дома"""
    
    def __init__(self, parent=None, text="Идет поиск дома..."):
        super().__init__(parent, width=300, height=120)
        
        self.setWindowTitle("Хоуминг")
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title = QLabel("Хоуминг")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        self.status_label = QLabel(text)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 12px; color: #5a6a7a;")
        layout.addWidget(self.status_label)
        
        self.dot_count = 0
        self.dot_timer = QTimer()
        self.dot_timer.timeout.connect(self._update_dots)
        self.dot_timer.start(500)
    
    def _update_dots(self):
        self.dot_count = (self.dot_count + 1) % 4
        dots = "." * self.dot_count
        base_text = self.status_label.text().split(".")[0]
        self.status_label.setText(base_text + dots)
    
    def set_text(self, text: str):
        self.status_label.setText(text)
    
    def done(self, result):
        self.dot_timer.stop()
        super().done(result)


class ErrorDialog(BaseDialog):
    """Диалог ошибки"""
    
    def __init__(self, parent=None, title="Ошибка", message="Произошла ошибка"):
        super().__init__(parent, width=350, height=150)
        
        self.setWindowTitle(title)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #c0392b;")
        layout.addWidget(title_label)
        
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("font-size: 13px; color: #34495e;")
        message_label.setWordWrap(True)
        layout.addWidget(message_label)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        ok_button = QPushButton("OK")
        ok_button.setStyleSheet("background-color: #bdcfdd; border: 2px solid #a6b8c6;")
        ok_button.clicked.connect(self.accept)
        ok_button.setDefault(True)
        button_layout.addWidget(ok_button)
        
        layout.addLayout(button_layout)


def show_error(parent, title="Ошибка", message="Произошла ошибка"):
    """Утилита для показа диалога ошибки"""
    dialog = ErrorDialog(parent, title, message)
    dialog.exec()