from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton
)
from PySide6.QtCore import Qt, QTimer


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
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Заголовок
        label = QLabel("Введите пароль для выхода:")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-weight: bold;")
        layout.addWidget(label)
        
        # Поле ввода
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.returnPressed.connect(self._check_password)
        layout.addWidget(self.password_input)
        
        # Сообщение об ошибке
        self.error_label = QLabel("Неверный пароль!")
        self.error_label.setStyleSheet("color: #e74c3c; font-size: 12px;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.hide()
        layout.addWidget(self.error_label)
        
        # Кнопки
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
    
    def _check_password(self) -> None:
        """Проверка пароля"""
        if self.password_input.text() == "1111":
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


class HomingDialog(BaseDialog):
    """Диалог поиска дома"""
    
    def __init__(self, parent=None, text="Идет поиск дома..."):
        super().__init__(parent, width=300, height=120)
        
        self.setWindowTitle("Хоуминг")
        
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Заголовок
        title = QLabel("Хоуминг")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title)
        
        # Статус
        self.status_label = QLabel(text)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 12px; color: #5a6a7a;")
        layout.addWidget(self.status_label)
        
        # Анимация точек
        self.dot_count = 0
        self.dot_timer = QTimer()
        self.dot_timer.timeout.connect(self._update_dots)
        self.dot_timer.start(500)
    
    def _update_dots(self) -> None:
        """Обновление анимации точек"""
        self.dot_count = (self.dot_count + 1) % 4
        dots = "." * self.dot_count
        base_text = self.status_label.text().split(".")[0]
        self.status_label.setText(base_text + dots)
    
    def set_text(self, text: str) -> None:
        """Обновление текста статуса"""
        self.status_label.setText(text)
    
    def done(self, result) -> None:
        """Останавливаем таймер при закрытии"""
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
        
        # Заголовок
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #c0392b;")
        layout.addWidget(title_label)
        
        # Сообщение
        message_label = QLabel(message)
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("font-size: 13px; color: #34495e;")
        message_label.setWordWrap(True)
        layout.addWidget(message_label)
        
        # Кнопка OK
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        ok_button = QPushButton("OK")
        ok_button.setStyleSheet("background-color: #bdcfdd; border: 2px solid #a6b8c6;")
        ok_button.clicked.connect(self.accept)
        ok_button.setDefault(True)
        button_layout.addWidget(ok_button)
        
        layout.addLayout(button_layout)


def show_error(parent, title="Ошибка", message="Произошла ошибка") -> None:
    """Утилита для показа диалога ошибки"""
    dialog = ErrorDialog(parent, title, message)
    dialog.exec()