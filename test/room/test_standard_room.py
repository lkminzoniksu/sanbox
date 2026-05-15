"""Tests for the StandardRoom class."""

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.StandardRoom import StandardRoom


class TestStandardRoom:
    """Tests for the StandardRoom class."""

    def setup_method(self) -> None:
        """Create reusable standard room."""
        self.room = StandardRoom(
            101,
            BedType.QUEEN,
            False,
        )

    def test_base_price(self) -> None:
        """Test the base price of a standard room."""
        assert self.room.base_price == 200.0

    def test_room_number(self) -> None:
        """Test the room number property."""
        assert self.room.room_number == 101

    def test_room_type(self) -> None:
        """Test the room type property."""
        assert self.room.room_type == RoomType.STANDARD

    def test_bed_type(self) -> None:
        """Test the bed type property."""
        assert self.room.bed_type == BedType.QUEEN

    def test_smoking(self) -> None:
        """Test the smoking property."""
        assert self.room.smoking is False

    def test_occupied_default(self) -> None:
        """Test that a new room is not occupied by default."""
        assert self.room.occupied is False

    def test_amenities_default_empty(self) -> None:
        """Test amenities start empty."""
        assert self.room.amenities == []

    def test_special_requests_default_empty(self) -> None:
        """Test special requests start empty."""
        assert self.room.special_requests == []

    def test_add_amenity(self) -> None:
        """Test adding an amenity to a room."""
        self.room.add_amenity(Amenity.POOL)

        assert Amenity.POOL in self.room.amenities

    def test_add_same_amenity_does_not_duplicate(self) -> None:
        """Test adding same amenity does not duplicate."""
        self.room.add_amenity(Amenity.POOL)
        self.room.add_amenity(Amenity.POOL)

        assert self.room.amenities.count(
            Amenity.POOL
        ) == 1

    def test_remove_amenity(self) -> None:
        """Test removing an amenity from a room."""
        self.room.add_amenity(Amenity.POOL)
        self.room.remove_amenity(Amenity.POOL)

        assert Amenity.POOL not in self.room.amenities

    def test_remove_missing_amenity(self) -> None:
        """Test removing a missing amenity does not fail."""
        self.room.remove_amenity(Amenity.POOL)

        assert Amenity.POOL not in self.room.amenities

    def test_add_special_request(self) -> None:
        """Test adding a special request."""
        self.room.add_special_request("Extra towels")

        assert "Extra towels" in self.room.special_requests

    def test_clear_special_requests(self) -> None:
        """Test clearing special requests."""
        self.room.add_special_request("Extra towels")
        self.room.clear_special_requests()

        assert self.room.special_requests == []

    def test_check_in(self) -> None:
        """Test checking in a room."""
        self.room.check_in()

        assert self.room.occupied is True

    def test_check_out(self) -> None:
        """Test checking out a room."""
        self.room.check_in()
        self.room.check_out()

        assert self.room.occupied is False

    def test_check_out_clears_special_requests(self) -> None:
        """Test checkout clears special requests."""
        self.room.add_special_request("Extra towels")
        self.room.check_out()

        assert self.room.special_requests == []

    def test_calculate_price_one_night(self) -> None:
        """Test calculating price for one night."""
        assert self.room.calculate_price(1) == 200.0

    def test_calculate_price_multiple_nights(self) -> None:
        """Test calculating price for multiple nights."""
        assert self.room.calculate_price(3) == 600.0

    def test_calculate_price_zero_nights(self) -> None:
        """Test calculating price for zero nights."""
        assert self.room.calculate_price(0) == 0.0

    def test_calculate_price_negative_nights(self) -> None:
        """Test calculating price for negative nights."""
        assert self.room.calculate_price(-2) == 0.0
