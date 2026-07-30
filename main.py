import sys
import os
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from PySide6.QtCore import Qt


def main() -> None:
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    os.environ["QT_VIRTUALKEYBOARD_AUTO_HIDE"] = "0"

    app = QApplication(sys.argv)

    app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)

    window = MainWindow()
    window.show()

    app.focusChanged.connect(_on_focus_changed)

    sys.exit(app.exec())

def _on_focus_changed(old, new):
    if new and hasattr(new, 'echoMode'):
        QGuiApplication.inputMethod().show()
        QGuiApplication.inputMethod().update(Qt.ImQueryAll)

if __name__ == "__main__":
    main()