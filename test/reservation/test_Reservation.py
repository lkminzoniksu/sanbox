"""Tests for the Reservation class."""

from datetime import date

import pytest

from src.hotel.data.customer.Customer import Customer
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.Status import Status
from src.hotel.data.reservation.Reservation import Reservation
from src.hotel.data.room.StandardRoom import StandardRoom
from src.hotel.data.room.DeluxeRoom import DeluxeRoom


class TestReservation:
    """Tests for the Reservation class."""

    def setup_method(self) -> None:
        """Create reusable test objects."""
        self.customer = Customer(
            "C001",
            "John Doe",
            "john@email.com",
            "1234567890",
            "123 Main St",
            0.10
        )
        self.room = StandardRoom(101, BedType.QUEEN, False)
        self.reservation = Reservation(
            "R001",
            self.customer,
            [self.room],
            date(2026, 5, 1),
            date(2026, 5, 4),
            date(2026, 4, 28)
        )

    def test_init(self) -> None:
        """Test reservation initialization."""
        assert self.reservation.reservation_id == "R001"
        assert self.reservation.guest == self.customer
        assert self.reservation.rooms == [self.room]
        assert self.reservation.checkin_date == date(2026, 5, 1)
        assert self.reservation.checkout_date == date(2026, 5, 4)
        assert self.reservation.booking_date == date(2026, 4, 28)
        assert self.reservation.status == Status.PENDING

    def test_set_checkin_date(self) -> None:
        """Test updating checkin date."""
        self.reservation.checkin_date = date(2026, 5, 2)
        assert self.reservation.checkin_date == date(2026, 5, 2)

    def test_set_checkout_date(self) -> None:
        """Test updating checkout date."""
        self.reservation.checkout_date = date(2026, 5, 5)
        assert self.reservation.checkout_date == date(2026, 5, 5)

    def test_set_status(self) -> None:
        """Test updating status."""
        self.reservation.status = Status.CONFIRMED
        assert self.reservation.status == Status.CONFIRMED

    def test_number_of_nights(self) -> None:
        """Test number of nights."""
        assert self.reservation.number_of_nights == 3

    def test_subtotal(self) -> None:
        """Test subtotal calculation."""
        assert self.reservation.subtotal == 600.0

    def test_discount_amount(self) -> None:
        """Test discount calculation."""
        assert self.reservation.discount_amount == 60.0

    def test_total_price(self) -> None:
        """Test total price after discount."""
        assert self.reservation.total_price == 540.0

    def test_confirm(self) -> None:
        """Test confirming a reservation."""
        self.reservation.confirm()
        assert self.reservation.status == Status.CONFIRMED

    def test_confirm_only_pending(self) -> None:
        """Test confirm does not change cancelled reservation."""
        self.reservation.cancel()
        self.reservation.confirm()
        assert self.reservation.status == Status.CANCELLED

    def test_cancel_pending(self) -> None:
        """Test cancelling pending reservation."""
        self.reservation.cancel()
        assert self.reservation.status == Status.CANCELLED

    def test_cancel_confirmed(self) -> None:
        """Test cancelling confirmed reservation."""
        self.reservation.confirm()
        self.reservation.cancel()
        assert self.reservation.status == Status.CANCELLED

    def test_check_in(self) -> None:
        """Test checking in reservation."""
        self.reservation.confirm()
        self.reservation.check_in()

        assert self.reservation.status == Status.CHECKED_IN
        assert self.room.occupied is True

    def test_check_in_without_confirm_raises_error(self) -> None:
        """Test check in fails if reservation is not confirmed."""
        with pytest.raises(ValueError):
            self.reservation.check_in()

    def test_check_out(self) -> None:
        """Test checking out reservation."""
        self.reservation.confirm()
        self.reservation.check_in()
        self.reservation.check_out()

        assert self.reservation.status == Status.CHECKED_OUT
        assert self.room.occupied is False

    def test_check_out_without_check_in_raises_error(self) -> None:
        """Test check out fails if reservation is not checked in."""
        with pytest.raises(ValueError):
            self.reservation.check_out()

    def test_add_room(self) -> None:
        """Test adding room to reservation."""
        room2 = DeluxeRoom(201, BedType.KING, False)
        self.reservation.add_room(room2)

        assert room2 in self.reservation.rooms

    def test_add_same_room_does_not_duplicate(self) -> None:
        """Test adding same room does not duplicate it."""
        self.reservation.add_room(self.room)

        assert len(self.reservation.rooms) == 1

    def test_add_occupied_room_raises_error(self) -> None:
        """Test adding occupied room raises error."""
        room2 = DeluxeRoom(201, BedType.KING, False)
        room2.check_in()

        with pytest.raises(ValueError):
            self.reservation.add_room(room2)

    def test_remove_room(self) -> None:
        """Test removing room from reservation."""
        self.reservation.remove_room(self.room)

        assert self.room not in self.reservation.rooms

    def test_invoice(self) -> None:
        """Test invoice output."""
        expected = (
            "Reservation #R001\n"
            "Guest: John Doe #C001\n"
            "Nights: 3\n"
            "Subtotal: $600.00\n"
            "Discount: $60.00\n"
            "Total: $540.00"
        )

        assert self.reservation.invoice == expected

    def test_str(self) -> None:
        """Test string representation."""
        assert str(self.reservation) == (
            "Reservation R001 - John Doe #C001 - Pending"
        )
