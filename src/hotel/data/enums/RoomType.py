"""Defines the RoomType enumeration for hotel rooms."""
from enum import Enum


class RoomType(Enum):
    """Enumeration representing room categories."""
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    SUITE = "Suite"
    PENTHOUSE = "Penthouse"

    def __str__(self) -> str:
        """Return the string representation of the room type."""
        return str(self.value)

    def __repr__(self) -> str:
        """Return the official string representation of the room type."""
        return str(self)
