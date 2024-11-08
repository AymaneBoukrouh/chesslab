from typing import TYPE_CHECKING

from PyQt6.QtWidgets import QWidget

from app.config import Config
from app.enums import ObjectType
from app.schemas import Cell
from app.types import Matrix
from app.utils import fen_to_matrix

from .pieces import Piece
from .pieces import PieceGenerator
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
        self._set_initial_position()

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

    def _set_initial_position(self):
        """sets the initial position of the pieces"""

        self.clear_pieces()
        self.set_position(Config.INITIAL_FEN_POSITION)

    def set_position(self, fen: str):  # TODO: proper type hint
        matrix: Matrix = fen_to_matrix(fen)
        for notation, piece_letter in matrix.items():
            if not piece_letter:
                continue

            self.set_piece(notation, piece_letter)

    def set_piece(self, notation: Cell.notation, piece_letter: str):
        """sets a piece on the board"""

        cell = Cell.from_notation(notation)
        PieceGenerator.from_letter(parent=self, letter=piece_letter, cell=cell)

    def clear_pieces(self):
        """clears all pieces from the board and deletes piece objects"""

        for piece in self.pieces:
            piece.setParent(None)
            del piece

    @property
    def pieces(self) -> list[Piece]:
        """returns all pieces on the board"""

        return self.findChildren(Piece)

    @property
    def pieces_count(self) -> int:
        """returns the number of pieces on the board"""

        return len(self.pieces)
