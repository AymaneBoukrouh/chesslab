from typing import TYPE_CHECKING

from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QWidget

from app.board import Board

if TYPE_CHECKING:
    from .main_window import MainWindow


class CentralWidget(QWidget):
    def __init__(self, parent: "MainWindow"):
        super().__init__()
        self._setup()

    def _setup(self):
        self._set_layout()
        self._set_board()

    def _set_layout(self):
        """configures layout"""

        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)

    def _set_board(self):
        """configures board"""

        self.board = Board(self)
        self.board.setFixedSize(self.board.width(), self.board.height())
        self.layout.addWidget(self.board)
