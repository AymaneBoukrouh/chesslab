from pydantic import BaseModel
from pydantic import field_validator


class Cell(BaseModel):
    """
    A cell is a file and rank pair, e.g. a1, b3, h4, etc.
    """

    file: str
    rank: int

    @field_validator("file")
    @classmethod
    def validate_file(cls, v: str) -> str:
        if v not in "abcdefgh":
            raise ValueError("File must be a letter between a and h.")
        return v

    @field_validator("rank")
    @classmethod
    def validate_rank(cls, v: int) -> int:
        if v not in range(1, 9):
            raise ValueError("Rank must be a number between 1 and 8.")
        return v

    @staticmethod
    def from_notation(notation: str) -> "Cell":
        return Cell(file=notation[0], rank=int(notation[1]))

    @property
    def notation(self) -> str:
        return f"{self.file}{self.rank}"
