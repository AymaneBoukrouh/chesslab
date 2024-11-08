from PyQt6.QtWidgets import QMainWindow

from app.config import Config


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup()

    def _setup(self):
        """configures window settings and styles"""

        self.setWindowTitle(Config.WINDOW_TITLE)
        self.showMaximized()
