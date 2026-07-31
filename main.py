import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from PySide6.QtCore import Qt


def main() -> None:

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()