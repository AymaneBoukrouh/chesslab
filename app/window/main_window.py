from PyQt6.QtWidgets import QMainWindow

from app.config import Config

from .central_widget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup()

    def _setup(self):
        self.setWindowTitle(Config.WINDOW_TITLE)
        self._set_style()
        self._set_central_widget()
        self.showMaximized()

    def _set_style(self):
        """configures window styles from css file"""

        with open(Config.WINDOW_STYLE_PATH) as f:
            self.setStyleSheet(f.read())

    def _set_central_widget(self):
        """configures the central widget containing the board"""

        self.setCentralWidget(CentralWidget(self))
