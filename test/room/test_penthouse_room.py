"""Tests for the PenthouseRoom class."""

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.PenthouseRoom import PenthouseRoom


class TestPenthouseRoom:
    """Tests for the PenthouseRoom class."""

    def test_base_price(self) -> None:
        """Test the base price of a penthouse room."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.base_price == 500.0

    def test_room_number(self) -> None:
        """Test the room number property."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.room_number == 401

    def test_room_type(self) -> None:
        """Test the room type property."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.room_type == RoomType.PENTHOUSE

    def test_bed_type(self) -> None:
        """Test the bed type property."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.bed_type == BedType.KING

    def test_smoking(self) -> None:
        """Test the smoking property."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.smoking is False

    def test_occupied_default(self) -> None:
        """Test that a new room is not occupied by default."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.occupied is False

    def test_add_amenity(self) -> None:
        """Test adding an amenity to a room."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.add_amenity(Amenity.JACUZZI)
        assert Amenity.JACUZZI in room.amenities

    def test_remove_amenity(self) -> None:
        """Test removing an amenity from a room."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.add_amenity(Amenity.JACUZZI)
        room.remove_amenity(Amenity.JACUZZI)
        assert Amenity.JACUZZI not in room.amenities

    def test_remove_missing_amenity(self) -> None:
        """Test removing a missing amenity does not fail."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.remove_amenity(Amenity.JACUZZI)
        assert Amenity.JACUZZI not in room.amenities

    def test_add_special_request(self) -> None:
        """Test adding a special request."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.add_special_request("Private dinner")
        assert "Private dinner" in room.special_requests

    def test_clear_special_requests(self) -> None:
        """Test clearing special requests."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.add_special_request("Private dinner")
        room.clear_special_requests()
        assert room.special_requests == []

    def test_check_in(self) -> None:
        """Test checking in a room."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.check_in()
        assert room.occupied is True

    def test_check_out(self) -> None:
        """Test checking out a room."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.check_in()
        room.check_out()
        assert room.occupied is False

    def test_check_out_clears_special_requests(self) -> None:
        """Test checkout clears special requests."""
        room = PenthouseRoom(401, BedType.KING, False)
        room.add_special_request("Private dinner")
        room.check_out()
        assert room.special_requests == []

    def test_calculate_price_one_night(self) -> None:
        """Test calculating price for one night."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.calculate_price(1) == 500.0

    def test_calculate_price_multiple_nights(self) -> None:
        """Test calculating price for multiple nights."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.calculate_price(3) == 1500.0

    def test_calculate_price_zero_nights(self) -> None:
        """Test calculating price for zero nights."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.calculate_price(0) == 0.0

    def test_calculate_price_negative_nights(self) -> None:
        """Test calculating price for negative nights."""
        room = PenthouseRoom(401, BedType.KING, False)
        assert room.calculate_price(-2) == 0.0
    