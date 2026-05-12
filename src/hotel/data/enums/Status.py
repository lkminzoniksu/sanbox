"""Defines the Status enumeration for reservations."""
from enum import Enum


class Status(Enum):
    """Enumeration representing reservation status."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CHECKED_IN = "Checked-in"
    CHECKED_OUT = "Checked-out"
    CANCELLED = "Cancelled"
    NO_SHOW = "No-show"

    def __str__(self) -> str:
        """Return the string representation of the status."""
        return str(self.value)

    def __repr__(self) -> str:
        """Return the official string representation of the status."""
        return str(self)
