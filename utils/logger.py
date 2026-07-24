from datetime import datetime
from typing import Optional
from PySide6.QtWidgets import QPlainTextEdit


class Logger:
    """Универсальный логгер с поддержкой Qt"""
    
    def __init__(self, widget: QPlainTextEdit):
        self.widget = widget
    
    def log(self, message: str, is_error: bool = False) -> None:
        """Запись в лог"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        color = "#e74c3c" if is_error else "#2c3e50"
        log_message = f'<span style="color: {color};">[{timestamp}] {message}</span>'
        
        self.widget.appendHtml(log_message)
        
        # Прокрутка вниз
        cursor = self.widget.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.widget.setTextCursor(cursor)
    
    def info(self, message: str) -> None:
        """Информационное сообщение"""
        self.log(message, is_error=False)
    
    def error(self, message: str) -> None:
        """Сообщение об ошибке"""
        self.log(message, is_error=True)