from typing import TYPE_CHECKING

from app.enums import PieceLetter
from app.schemas import Cell

from .base import Piece
from .types import Bishop
from .types import King
from .types import Knight
from .types import Pawn
from .types import Queen
from .types import Rook

if TYPE_CHECKING:
    from ..board import Board


class PieceGenerator:
    PIECE_CLASS_MAP = {
        PieceLetter.K: King,
        PieceLetter.Q: Queen,
        PieceLetter.R: Rook,
        PieceLetter.B: Bishop,
        PieceLetter.N: Knight,
        PieceLetter.P: Pawn,
    }

    @staticmethod
    def from_letter(parent: "Board", letter: PieceLetter, cell: Cell) -> "Piece":
        """creates a piece from a letter"""

        # get color
        color = letter.isupper()  # upppercase means light, lowercase means dark

        # get corresponding piece class
        piece_class = PieceGenerator.PIECE_CLASS_MAP[letter.upper()]

        # set letter attribute
        piece_class.letter = letter

        # create and return piece instance
        return piece_class(parent=parent, cell=cell, color=color)
