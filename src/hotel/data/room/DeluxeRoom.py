"""Deluxe room class for the hotel system."""

from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.Room import Room


class DeluxeRoom(Room):
    """Represents a deluxe hotel room."""

    def __init__(
        self,
        room_number: int,
        bed_type: BedType,
        smoking: bool,
    ) -> None:
        """Initialize a deluxe room with basic attributes."""

        super().__init__(
            room_number,
            bed_type,
            smoking,
            RoomType.DELUXE,
        )

    @property
    def base_price(self) -> float:
        """Return the base price of the deluxe room."""

        return 300.0
