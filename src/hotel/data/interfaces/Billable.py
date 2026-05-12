"""Billable interface for hotel system."""

from abc import ABC, abstractmethod


class Billable(ABC):
    """Interface for objects that can be billed."""

    @abstractmethod
    def calculate_price(self, nights: int) -> float:
        """Calculate and return the total price."""
        raise NotImplementedError
