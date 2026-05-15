"""Abstract base class for room types."""

from abc import ABC, abstractmethod
from typing import List

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.interfaces.Billable import Billable


class Room(Billable, ABC):
    """Abstract class representing a hotel room."""

    def __init__(
        self,
        room_number: int,
        bed_type: BedType,
        smoking: bool,
        room_type: RoomType,
    ) -> None:
        """Initialize a room with basic attributes."""
        self._room_number = room_number
        self._bed_type = bed_type
        self._room_type = room_type
        self._amenities: List[Amenity] = []
        self._smoking = smoking
        self._occupied = False
        self._special_requests: List[str] = []

    @property
    def room_number(self) -> int:
        """Return the room number."""
        return self._room_number

    @property
    def room_type(self) -> RoomType:
        """Return the room type."""
        return self._room_type

    @property
    def bed_type(self) -> BedType:
        """Return the bed type."""
        return self._bed_type

    @property
    def amenities(self) -> List[Amenity]:
        """Return the room amenities."""
        return self._amenities.copy()

    @property
    def smoking(self) -> bool:
        """Return whether the room allows smoking."""
        return self._smoking

    @property
    def occupied(self) -> bool:
        """Return whether the room is occupied."""
        return self._occupied

    def add_amenity(self, amenity: Amenity) -> None:
        """Add an amenity to the room."""
        if amenity not in self._amenities:
            self._amenities.append(amenity)

    def remove_amenity(self, amenity: Amenity) -> None:
        """Remove an amenity from the room."""
        if amenity in self._amenities:
            self._amenities.remove(amenity)

    @property
    def special_requests(self) -> List[str]:
        """Return the room special requests."""
        return self._special_requests.copy()

    def add_special_request(self, request: str) -> None:
        """Add a special request to the room."""
        self._special_requests.append(request)

    def clear_special_requests(self) -> None:
        """Clear all special requests from the room."""
        self._special_requests.clear()

    def check_in(self) -> None:
        """Mark the room as occupied."""
        self._occupied = True

    def check_out(self) -> None:
        """Mark the room as not occupied."""
        self._occupied = False
        self.clear_special_requests()

    @property
    @abstractmethod
    def base_price(self) -> float:
        """Return the base price of the room."""
        raise NotImplementedError

    def calculate_price(self, nights: int) -> float:
        """Return the total price for the stay."""
        if nights <= 0:
            return 0.0

        return self.base_price * nights

    def __str__(self) -> str:
        """Return the string representation of the room."""
        return (
            f"Room {self._room_number} - {self._room_type} - "
            f"{self._bed_type} - "
            f"{'Smoking' if self._smoking else 'Non-smoking'}"
        )
