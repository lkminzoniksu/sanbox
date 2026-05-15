"""Hotel class for the hotel system."""

from typing import List, Optional

from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.reservation.Reservation import Reservation
from src.hotel.data.room.Room import Room


class Hotel:
    """Represents a hotel system."""
    def __init__(self) -> None:
        """Initialize the hotel with empty room and reservation lists."""
        self._rooms: List[Room] = []
        self._reservations: List[Reservation] = []

    @property
    def rooms(self) -> List[Room]:
        """Return the hotel rooms."""
        return self._rooms.copy()

    @property
    def reservations(self) -> List[Reservation]:
        """Return the hotel reservations."""
        return self._reservations.copy()

    def add_room(self, room: Room) -> None:
        """Add a room to the hotel."""
        if room not in self._rooms:
            self._rooms.append(room)

    def remove_room(self, room_number: int) -> None:
        """Remove a room from the hotel by room number."""
        room = self.find_room(room_number)
        if room is not None:
            self._rooms.remove(room)

    def find_room(self, room_number: int) -> Optional[Room]:
        """Find a room by room number."""
        for room in self._rooms:
            if room.room_number == room_number:
                return room
        return None

    def find_available_rooms(self) -> List[Room]:
        """Return all available rooms."""
        available: List[Room] = []
        for room in self._rooms:
            if not room.occupied:
                available.append(room)
        return available

    def find_available_rooms_by_type(self, room_type: RoomType) -> List[Room]:
        """Return all available rooms of a given type."""
        available: List[Room] = []
        for room in self._rooms:
            if not room.occupied and room.room_type == room_type:
                available.append(room)
        return available

    def create_reservation(self, reservation: Reservation) -> None:
        """Add a reservation to the hotel."""
        if reservation not in self._reservations:
            self._reservations.append(reservation)

    def cancel_reservation(self, reservation_id: str) -> None:
        """Cancel a reservation by reservation id."""
        reservation = self.find_reservation(reservation_id)
        if reservation is not None:
            reservation.cancel()

    def find_reservation(self, reservation_id: str) -> Optional[Reservation]:
        """Find a reservation by reservation id."""
        for reservation in self._reservations:
            if reservation.reservation_id == reservation_id:
                return reservation
        return None

    def __str__(self) -> str:
        """Return the string representation of the hotel."""
        return (
            f"Hotel with {len(self._rooms)} rooms and "
            f"{len(self._reservations)} reservations"
        )
