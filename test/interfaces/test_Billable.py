"""Tests for the Billable interface."""

import pytest

from src.hotel.data.enums.BedType import BedType
from src.hotel.data.interfaces.Billable import Billable
from src.hotel.data.room.DeluxeRoom import DeluxeRoom
from src.hotel.data.room.PenthouseRoom import PenthouseRoom
from src.hotel.data.room.StandardRoom import StandardRoom
from src.hotel.data.room.SuiteRoom import SuiteRoom


class TestBillable:
    """Tests for the Billable interface."""

    def test_cannot_instantiate(self) -> None:
        """Test that Billable cannot be instantiated."""
        with pytest.raises(TypeError):
            Billable()

    def test_standard_room_is_billable(self) -> None:
        """Test StandardRoom implements Billable."""
        room = StandardRoom(
            101,
            BedType.QUEEN,
            False,
        )

        assert hasattr(room, "calculate_price")

    def test_deluxe_room_is_billable(self) -> None:
        """Test DeluxeRoom implements Billable."""
        room = DeluxeRoom(
            201,
            BedType.KING,
            False,
        )

        assert hasattr(room, "calculate_price")

    def test_suite_room_is_billable(self) -> None:
        """Test SuiteRoom implements Billable."""
        room = SuiteRoom(
            301,
            BedType.KING,
            True,
        )

        assert hasattr(room, "calculate_price")

    def test_penthouse_room_is_billable(self) -> None:
        """Test PenthouseRoom implements Billable."""
        room = PenthouseRoom(
            701,
            BedType.KING,
            False,
        )

        assert hasattr(room, "calculate_price")

    def test_standard_room_price(self) -> None:
        """Test StandardRoom pricing."""
        room = StandardRoom(
            101,
            BedType.QUEEN,
            False,
        )

        assert room.calculate_price(2) == 400.0

    def test_deluxe_room_price(self) -> None:
        """Test DeluxeRoom pricing."""
        room = DeluxeRoom(
            201,
            BedType.KING,
            False,
        )

        assert room.calculate_price(2) == 600.0

    def test_suite_room_price(self) -> None:
        """Test SuiteRoom pricing."""
        room = SuiteRoom(
            301,
            BedType.KING,
            True,
        )

        assert room.calculate_price(2) == 800.0

    def test_penthouse_room_price(self) -> None:
        """Test PenthouseRoom pricing."""
        room = PenthouseRoom(
            701,
            BedType.KING,
            False,
        )

        assert room.calculate_price(2) == 1000.0
