"""Tests for the Hotel class."""

from datetime import date

from src.hotel.data.customer.Customer import Customer
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.hotel.Hotel import Hotel
from src.hotel.data.reservation.Reservation import Reservation
from src.hotel.data.room.DeluxeRoom import DeluxeRoom
from src.hotel.data.room.PenthouseRoom import PenthouseRoom
from src.hotel.data.room.StandardRoom import StandardRoom


class TestHotel:
    """Tests for the Hotel class."""
    def setup_method(self) -> None:
        """Create reusable test data."""
        self.hotel = Hotel()

        self.room1 = StandardRoom(
            101,
            BedType.QUEEN,
            False,
        )

        self.room2 = DeluxeRoom(
            201,
            BedType.KING,
            False,
        )

        self.room4 = PenthouseRoom(
            701,
            BedType.KING,
            False,
        )

        self.customer = Customer(
            "C001",
            "John Doe",
            "john@email.com",
            "1234567890",
            "123 Main St",
            0.10,
        )

        self.reservation = Reservation(
            "R001",
            self.customer,
            [self.room1],
            date(2026, 5, 1),
            date(2026, 5, 4),
            date(2026, 4, 28),
        )

    def test_penthouse_check_in(self) -> None:
        """Test penthouse check-in."""
        self.hotel.add_room(
            self.room4,
        )

        self.room4.check_in()

        assert self.room4.occupied is True

    def test_penthouse_check_out(self) -> None:
        """Test penthouse check-out."""
        self.hotel.add_room(
            self.room4,
        )

        self.room4.check_in()
        self.room4.check_out()

        assert self.room4.occupied is False

    def test_reservation_guest(self) -> None:
        """Test reservation guest."""
        assert self.reservation.guest == self.customer

    def test_reservation_room(self) -> None:
        """Test reservation room."""
        assert self.room1 in self.reservation.rooms

    def test_hotel_room_count(self) -> None:
        """Test hotel room count."""
        self.hotel.add_room(
            self.room1,
        )

        self.hotel.add_room(
            self.room2,
        )

        assert len(self.hotel.rooms) == 2

    def test_hotel_reservation_count(self) -> None:
        """Test hotel reservation count."""
        self.hotel.create_reservation(
            self.reservation,
        )

        assert len(
            self.hotel.reservations,
        ) == 1
