from typing import TYPE_CHECKING

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QFrame

from app.config import Config

if TYPE_CHECKING:
    from .board import Board


class Square(QFrame):
    def __init__(self, parent: "Board", x: int, y: int):
        super().__init__(parent)
        self._setup(x, y)

    def _setup(self, x: int, y: int):
        self._set_cell(x, y)
        self._set_color(x, y)
        self._set_size_and_position(x, y)

    def _set_cell(self, x: int, y: int):
        """configures square properties"""

        self.file = chr(ord("a") + x)  # vertical columns, labeled a through h
        self.rank = (
            8 - y
        )  # horizontal rows, numbered 1 through 8, starting from white (bottom)
        self.cell = f"{self.file}{self.rank}"  # cell name, e.g. a1, b3, h4, etc.
        self.setObjectName(self.cell)

    def _set_color(self, x: int, y: int):
        """configures square color based on position"""

        if x % 2 == y % 2:
            self.setProperty("color", "light-square")
        else:
            self.setProperty("color", "dark-square")

    def _set_size_and_position(self, x: int, y: int):
        """configures square size and position"""

        ss = Config.SQUARE_SIZE
        self.setGeometry(QRect(x * ss, y * ss, ss, ss))