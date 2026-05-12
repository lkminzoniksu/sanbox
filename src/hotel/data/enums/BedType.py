"""Defines the Bed Type enuaration for the hotel romms."""
from enum import Enum


class BedType(str, Enum):
    """Enumeration representing available bed types."""

    TWIN = "Twin"
    QUEEN = "Queen"
    KING = "King"

    def __str__(self) -> str:
        """Return the string representation of the bed type."""
        return str(self.value)

    def __repr__(self) -> str:
        """Return the official string representation of the bed type."""
        return str(self)
