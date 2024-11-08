from enum import StrEnum


class PieceLetter(StrEnum):
    """
    Represents a piece type/color by a single letter.

    Light pieces are represented by upppercase letters.
    Dark pieces are represented by lowercase letters.

    P/p - Pawn
    N/n - Knight
    B/b - Bishop
    R/r - Rook
    Q/q - Queen
    K/k - King
    """

    P, p = "P", "p"
    N, n = "N", "n"
    B, b = "B", "b"
    R, r = "R", "r"
    Q, q = "Q", "q"
    K, k = "K", "k"
