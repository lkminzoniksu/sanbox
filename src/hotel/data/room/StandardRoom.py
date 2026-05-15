"""Standard room class for the hotel system."""

from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.Room import Room


class StandardRoom(Room):
    """Represents a standard hotel room."""
    def __init__(
        self,
        room_number: int,
        bed_type: BedType,
        smoking: bool,
    ) -> None:
        """Initialize a standard room with basic attributes."""
        super().__init__(
            room_number,
            bed_type,
            smoking,
            RoomType.STANDARD,
        )

    @property
    def base_price(self) -> float:
        """Return the base price of the standard room."""
        return 200.0
