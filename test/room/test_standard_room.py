"""Tests for the StandardRoom class."""

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.StandardRoom import StandardRoom


class TestStandardRoom:
    """Tests for the StandardRoom class."""

    def test_base_price(self) -> None:
        """Test the base price of a standard room."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.base_price == 200.0

    def test_room_number(self) -> None:
        """Test the room number property."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.room_number == 101

    def test_room_type(self) -> None:
        """Test the room type property."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.room_type == RoomType.STANDARD

    def test_bed_type(self) -> None:
        """Test the bed type property."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.bed_type == BedType.QUEEN

    def test_smoking(self) -> None:
        """Test the smoking property."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.smoking is False

    def test_occupied_default(self) -> None:
        """Test that a new room is not occupied by default."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.occupied is False

    def test_add_amenity(self) -> None:
        """Test adding an amenity to a room."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.add_amenity(Amenity.POOL)
        assert Amenity.POOL in room.amenities

    def test_remove_amenity(self) -> None:
        """Test removing an amenity from a room."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.add_amenity(Amenity.POOL)
        room.remove_amenity(Amenity.POOL)
        assert Amenity.POOL not in room.amenities

    def test_remove_missing_amenity(self) -> None:
        """Test removing a missing amenity does not fail."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.remove_amenity(Amenity.POOL)
        assert Amenity.POOL not in room.amenities

    def test_add_special_request(self) -> None:
        """Test adding a special request."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.add_special_request("Extra towels")
        assert "Extra towels" in room.special_requests

    def test_clear_special_requests(self) -> None:
        """Test clearing special requests."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.add_special_request("Extra towels")
        room.clear_special_requests()
        assert room.special_requests == []

    def test_check_in(self) -> None:
        """Test checking in a room."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.check_in()
        assert room.occupied is True

    def test_check_out(self) -> None:
        """Test checking out a room."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.check_in()
        room.check_out()
        assert room.occupied is False

    def test_check_out_clears_special_requests(self) -> None:
        """Test checkout clears special requests."""
        room = StandardRoom(101, BedType.QUEEN, False)
        room.add_special_request("Extra towels")
        room.check_out()
        assert room.special_requests == []

    def test_calculate_price_one_night(self) -> None:
        """Test calculating price for one night."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.calculate_price(1) == 200.0

    def test_calculate_price_multiple_nights(self) -> None:
        """Test calculating price for multiple nights."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.calculate_price(3) == 600.0

    def test_calculate_price_zero_nights(self) -> None:
        """Test calculating price for zero nights."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.calculate_price(0) == 0.0

    def test_calculate_price_negative_nights(self) -> None:
        """Test calculating price for negative nights."""
        room = StandardRoom(101, BedType.QUEEN, False)
        assert room.calculate_price(-2) == 0.0
