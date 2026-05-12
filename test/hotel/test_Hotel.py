"""Tests for the Hotel class."""

from datetime import date

from src.hotel.data.customer.Customer import Customer
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.enums.Status import Status
from src.hotel.data.hotel.Hotel import Hotel
from src.hotel.data.reservation.Reservation import Reservation
from src.hotel.data.room.DeluxeRoom import DeluxeRoom
from src.hotel.data.room.StandardRoom import StandardRoom
from src.hotel.data.room.SuiteRoom import SuiteRoom


class TestHotel:
    """Tests for the Hotel class."""

    def setup_method(self) -> None:
        """Create reusable test objects."""
        self.hotel = Hotel()
        self.room1 = StandardRoom(101, BedType.QUEEN, False)
        self.room2 = DeluxeRoom(201, BedType.KING, False)
        self.room3 = SuiteRoom(301, BedType.KING, True)

        self.customer = Customer(
            "C001",
            "John Doe",
            "john@email.com",
            "1234567890",
            "123 Main St"
        )

        self.reservation = Reservation(
            "R001",
            self.customer,
            [self.room1],
            date(2026, 5, 1),
            date(2026, 5, 3),
            date(2026, 4, 28)
        )

    def test_init(self) -> None:
        """Test hotel initialization."""
        assert self.hotel.rooms == []
        assert self.hotel.reservations == []

    def test_add_room(self) -> None:
        """Test adding a room."""
        self.hotel.add_room(self.room1)

        assert self.room1 in self.hotel.rooms

    def test_add_same_room_does_not_duplicate(self) -> None:
        """Test adding same room does not duplicate it."""
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room1)

        assert len(self.hotel.rooms) == 1

    def test_remove_room(self) -> None:
        """Test removing a room by room number."""
        self.hotel.add_room(self.room1)
        self.hotel.remove_room(101)

        assert self.room1 not in self.hotel.rooms

    def test_remove_missing_room_does_not_fail(self) -> None:
        """Test removing a room that does not exist."""
        self.hotel.remove_room(999)

        assert self.hotel.rooms == []

    def test_find_room(self) -> None:
        """Test finding a room by room number."""
        self.hotel.add_room(self.room1)

        assert self.hotel.find_room(101) == self.room1

    def test_find_missing_room(self) -> None:
        """Test finding a room that does not exist."""
        assert self.hotel.find_room(999) is None

    def test_find_available_rooms(self) -> None:
        """Test finding all available rooms."""
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)
        self.room2.check_in()

        available = self.hotel.find_available_rooms()

        assert self.room1 in available
        assert self.room2 not in available

    def test_find_available_rooms_by_type(self) -> None:
        """Test finding available rooms by room type."""
        self.hotel.add_room(self.room1)
        self.hotel.add_room(self.room2)
        self.hotel.add_room(self.room3)

        available = self.hotel.find_available_rooms_by_type(RoomType.DELUXE)

        assert self.room2 in available
        assert self.room1 not in available
        assert self.room3 not in available

    def test_find_available_rooms_by_type_excludes_occupied(self) -> None:
        """Test room type search excludes occupied rooms."""
        self.hotel.add_room(self.room2)
        self.room2.check_in()

        available = self.hotel.find_available_rooms_by_type(RoomType.DELUXE)

        assert available == []

    def test_create_reservation(self) -> None:
        """Test creating a reservation."""
        self.hotel.create_reservation(self.reservation)

        assert self.reservation in self.hotel.reservations

    def test_create_same_reservation_does_not_duplicate(self) -> None:
        """Test same reservation does not duplicate."""
        self.hotel.create_reservation(self.reservation)
        self.hotel.create_reservation(self.reservation)

        assert len(self.hotel.reservations) == 1

    def test_find_reservation(self) -> None:
        """Test finding a reservation by id."""
        self.hotel.create_reservation(self.reservation)

        assert self.hotel.find_reservation("R001") == self.reservation

    def test_find_missing_reservation(self) -> None:
        """Test finding a missing reservation."""
        assert self.hotel.find_reservation("BAD") is None

    def test_cancel_reservation(self) -> None:
        """Test cancelling a reservation."""
        self.hotel.create_reservation(self.reservation)
        self.hotel.cancel_reservation("R001")

        assert self.reservation.status == Status.CANCELLED

    def test_cancel_missing_reservation_does_not_fail(self) -> None:
        """Test cancelling a missing reservation does not fail."""
        self.hotel.cancel_reservation("BAD")

        assert self.hotel.reservations == []

    def test_str(self) -> None:
        """Test string representation."""
        self.hotel.add_room(self.room1)
        self.hotel.create_reservation(self.reservation)

        assert str(self.hotel) == "Hotel with 1 rooms and 1 reservations"
