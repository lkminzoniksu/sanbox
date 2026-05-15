"""Tests for the Room base class."""

import pytest

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.Room import Room


class DummyRoom(Room):
    """Concrete room used for testing."""

    @property
    def base_price(self) -> float:
        """Return dummy base price."""
        return 100.0


class TestRoom:
    """Tests for the Room base class."""

    def setup_method(self) -> None:
        """Create reusable room."""
        self.room = DummyRoom(
            999,
            BedType.QUEEN,
            False,
            RoomType.STANDARD,
        )

    def test_room_number(self) -> None:
        """Test room number."""
        assert self.room.room_number == 999

    def test_room_type(self) -> None:
        """Test room type."""
        assert self.room.room_type == RoomType.STANDARD

    def test_bed_type(self) -> None:
        """Test bed type."""
        assert self.room.bed_type == BedType.QUEEN

    def test_smoking(self) -> None:
        """Test smoking status."""
        assert self.room.smoking is False

    def test_occupied_default(self) -> None:
        """Test default occupied status."""
        assert self.room.occupied is False

    def test_amenities_default_empty(self) -> None:
        """Test default amenities."""
        assert self.room.amenities == []

    def test_add_amenity(self) -> None:
        """Test adding amenity."""
        self.room.add_amenity(Amenity.POOL)

        assert Amenity.POOL in self.room.amenities

    def test_add_same_amenity_does_not_duplicate(self) -> None:
        """Test adding the same amenity does not duplicate it."""
        self.room.add_amenity(Amenity.POOL)
        self.room.add_amenity(Amenity.POOL)

        assert self.room.amenities.count(Amenity.POOL) == 1

    def test_remove_amenity(self) -> None:
        """Test removing amenity."""
        self.room.add_amenity(Amenity.POOL)
        self.room.remove_amenity(Amenity.POOL)

        assert Amenity.POOL not in self.room.amenities

    def test_remove_missing_amenity(self) -> None:
        """Test removing missing amenity does not fail."""
        self.room.remove_amenity(Amenity.POOL)

        assert Amenity.POOL not in self.room.amenities

    def test_special_requests_default_empty(self) -> None:
        """Test default special requests."""
        assert self.room.special_requests == []

    def test_add_special_request(self) -> None:
        """Test adding special request."""
        self.room.add_special_request("Extra towels")

        assert "Extra towels" in self.room.special_requests

    def test_clear_special_requests(self) -> None:
        """Test clearing special requests."""
        self.room.add_special_request("Extra towels")
        self.room.clear_special_requests()

        assert self.room.special_requests == []

    def test_check_in(self) -> None:
        """Test check in."""
        self.room.check_in()

        assert self.room.occupied is True

    def test_check_out(self) -> None:
        """Test check out."""
        self.room.check_in()
        self.room.check_out()

        assert self.room.occupied is False

    def test_check_out_clears_requests(self) -> None:
        """Test checkout clears requests."""
        self.room.add_special_request("Extra towels")
        self.room.check_out()

        assert self.room.special_requests == []

    def test_calculate_price(self) -> None:
        """Test calculate price."""
        assert self.room.calculate_price(3) == 300.0

    def test_calculate_price_zero_nights(self) -> None:
        """Test zero nights."""
        assert self.room.calculate_price(0) == 0.0

    def test_calculate_price_negative_nights(self) -> None:
        """Test negative nights."""
        assert self.room.calculate_price(-2) == 0.0

    def test_str(self) -> None:
        """Test string representation."""
        assert str(self.room) == (
            "Room 999 - Standard - Queen - Non-smoking"
        )

    def test_cannot_instantiate_abstract_room(self) -> None:
        """Test abstract Room cannot instantiate."""
        with pytest.raises(TypeError):
            Room(
                1,
                BedType.QUEEN,
                False,
                RoomType.STANDARD,
            )
