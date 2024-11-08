from app.enums import PieceLetter
from app.schemas import Cell

type Matrix = dict[Cell.notation, PieceLetter]  # TODO: proper type hint
