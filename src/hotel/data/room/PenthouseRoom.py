"""Penthouse room class for the hotel system."""

from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.Room import Room


class PenthouseRoom(Room):
    """Represents a penthouse hotel room."""

    def __init__(
        self,
        room_number: int,
        bed_type: BedType,
        smoking: bool,
    ) -> None:
        """Initialize a penthouse room with basic attributes."""
        
        super().__init__(
            room_number,
            bed_type,
            smoking,
            RoomType.PENTHOUSE,
        )

    @property
    def base_price(self) -> float:
        """Return the base price of the penthouse room."""

        return 500.0
