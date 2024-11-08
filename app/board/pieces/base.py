from typing import TYPE_CHECKING

from PyQt6.QtSvgWidgets import QSvgWidget

from app.config import Config
from app.enums import PieceColor
from app.schemas import Cell

from ..square import Square

if TYPE_CHECKING:
    from ..board import Board


class Piece(QSvgWidget):
    def __init__(self, parent: "Board", color: PieceColor, cell: Cell):
        super().__init__(parent)
        self._setup(color, cell)

    def _setup(self, color: PieceColor, cell: Cell):
        self.setStyleSheet("background-color: none")
        self._set_size()
        self._set_color(color)
        self._set_cell(cell)
        self._set_svg()
        self.show()

    def _set_size(self):
        ss = Config.SQUARE_SIZE
        self.resize(ss, ss)

    def _set_color(self, color: PieceColor):
        """sets the color of the piece"""

        self.color = color

    def _set_cell(self, cell: Cell):
        """places the piece on the specified cell"""

        self.cell = cell
        self.setObjectName(cell.notation)
        self.move_to(cell)

    def _set_svg(self):
        """sets the svg of the piece"""

        self.load(f"{Config.PIECES_SVG_PATH}/{self.letter}.svg")

    def move_to(self, cell: Cell):
        """moves the piece to the specified cell"""

        cell_widget = self.parent().findChild(Square, cell.notation)
        self.move(cell_widget.pos())
