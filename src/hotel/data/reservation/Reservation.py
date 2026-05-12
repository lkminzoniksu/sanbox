"""Reservation class for the hotel system."""

from datetime import date
from typing import List
from src.hotel.data.enums.Status import Status
from src.hotel.data.customer.Customer import Customer
from src.hotel.data.room.Room import Room


class Reservation:
    """Represents a hotel reservation."""

    def __init__(
        self,
        reservation_id: str,
        guest: Customer,
        rooms: List[Room],
        checkin_date: date,
        checkout_date: date,
        booking_date: date,
        status: Status = Status.PENDING,
    ) -> None:

        """Initialize a reservation with basic attributes."""

        self._reservation_id = reservation_id
        self._guest = guest
        self._rooms = rooms.copy()
        self._checkin_date = checkin_date
        self._checkout_date = checkout_date
        self._booking_date = booking_date
        self._status = status

    @property
    def reservation_id(self) -> str:
        """Return the reservation id."""

        return self._reservation_id

    @property
    def guest(self) -> Customer:
        """Return the guest."""

        return self._guest

    @property
    def checkin_date(self) -> date:
        """Return the checkin date."""

        return self._checkin_date

    @checkin_date.setter
    def checkin_date(self, value: date) -> None:
        """Update the checkin date."""

        self._checkin_date = value

    @property
    def checkout_date(self) -> date:
        """Return the check out date."""

        return self._checkout_date

    @checkout_date.setter
    def checkout_date(self, value: date) -> None:
        """Update the checkout date."""

        self._checkout_date = value
        
    @property
    def booking_date(self) -> date:
        """Return the booking date."""

        return self._booking_date

    @property
    def status(self) -> Status:
        """Return the booking status."""

        return self._status

    @status.setter
    def status(self, value: Status) -> None:
        """Update the booking status."""

        self._status = value

    @property
    def number_of_nights(self) -> int:
        """Return the number of nights for the reservation."""

        return (self._checkout_date - self._checkin_date).days

    @property
    def subtotal(self) -> float:
        """Return the subtotal for all reserved rooms."""

        total = 0.0
        for room in self._rooms:
            total += room.calculate_price(self.number_of_nights)
        return total

    @property
    def discount_amount(self) -> float:
        """Return the discount amount."""
        #discount must be 0.value
        return self.subtotal * self._guest.discount

    @property
    def total_price(self) -> float:
        """Return the total price after discount."""

        return self.subtotal - self.discount_amount

    def confirm(self) -> None:
        """Confirm the reservation."""

        if self._status == Status.PENDING:
            self._status = Status.CONFIRMED

    def cancel(self) -> None:
        """Cancel the reservation."""

        if self._status in (Status.PENDING, Status.CONFIRMED):
            self._status = Status.CANCELLED

    def check_in(self) -> None:
        """Check in the reservation."""

        if self._status != Status.CONFIRMED:
            raise ValueError("Reservation must be confirmed first.")

        self._status = Status.CHECKED_IN
        for room in self._rooms:
            room.check_in()

    def check_out(self) -> None:
        """Check out the reservation."""

        if self._status != Status.CHECKED_IN:
            raise ValueError("Reservation must be checked in first.")

        self._status = Status.CHECKED_OUT
        for room in self._rooms:
            room.check_out()

    @property
    def rooms(self) -> List[Room]:
        """Return the reserved rooms."""

        return self._rooms.copy()

    def add_room(self, room: Room) -> None:
        """Add a room to the reservation."""

        if room in self._rooms:
            return

        if room.occupied:
            raise ValueError("Room is already occupied.")

        self._rooms.append(room)

    def remove_room(self, room: Room) -> None:
        """Remove a room from the reservation."""

        if room in self._rooms:
            self._rooms.remove(room)

    @property
    def invoice(self) -> str:
        """Return the reservation invoice."""
        return (
            f"Reservation #{self._reservation_id}\n"
            f"Guest: {self._guest}\n"
            f"Nights: {self.number_of_nights}\n"
            f"Subtotal: ${self.subtotal:.2f}\n"
            f"Discount: ${self.discount_amount:.2f}\n"
            f"Total: ${self.total_price:.2f}"
        )

    def __str__(self) -> str:
        """Return the string representation of the reservation."""
        return (
            f"Reservation {self._reservation_id} - "
            f"{self._guest} - {self._status}"
        )
