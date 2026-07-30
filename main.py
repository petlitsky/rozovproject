import sys
import os
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from PySide6.QtCore import Qt


def main() -> None:
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    app = QApplication(sys.argv)
    app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()