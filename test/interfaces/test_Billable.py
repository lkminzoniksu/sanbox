"""Tests for the Billable interface."""

import pytest

from src.hotel.data.interfaces.Billable import Billable
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.room.StandardRoom import StandardRoom


class TestBillable:
    """Tests for the Billable interface."""

    def test_cannot_instantiate(self) -> None:
        """Test that Billable cannot be instantiated."""
        with pytest.raises(TypeError):
            Billable()

    def test_room_is_billable(self) -> None:
        """Test that Room subclasses implement Billable."""
        room = StandardRoom(101, BedType.QUEEN, False)

        # If this works, Billable is correctly implemented
        assert hasattr(room, "calculate_price")

    def test_calculate_price_through_interface(self) -> None:
        """Test calculate_price behavior via Billable."""
        room = StandardRoom(101, BedType.QUEEN, False)

        assert room.calculate_price(2) == 400.0
