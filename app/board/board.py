from typing import TYPE_CHECKING

from PyQt6.QtWidgets import QWidget

from app.config import Config
from app.enums import ObjectType

from .square import Square

if TYPE_CHECKING:
    from app.window.central_widget import CentralWidget


class Board(QWidget):
    def __init__(self, parent: "CentralWidget"):
        super().__init__(parent)
        self._setup()

    def _setup(self):
        self.setObjectName(ObjectType.BOARD.value)
        self._set_style()
        self._set_size()
        self._set_squares()

    def _set_style(self):
        """configures board styles from css file"""

        with open(Config.BOARD_STYLE_PATH) as f:
            self.setStyleSheet(f.read())

    def _set_size(self):
        """sets the board size based on square size"""

        ss = Config.SQUARE_SIZE
        self.resize(ss * 8, ss * 8)

    def _set_squares(self):
        """creates 64 square objects (8x8)"""

        for x in range(8):
            for y in range(8):
                Square(self, x, y)  # square automatically sets its own color
