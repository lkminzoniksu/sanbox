"""Suite room class for the hotel system."""

from src.hotel.data.enums.BedType import BedType
from src.hotel.data.enums.RoomType import RoomType
from src.hotel.data.room.Room import Room


class SuiteRoom(Room):
    """Represents a suite hotel room."""

    def __init__(
        self,
        room_number: int,
        bed_type: BedType,
        smoking: bool,
    ) -> None:
        """Initialize a suite room with basic attributes."""

        super().__init__(
            room_number,
            bed_type,
            smoking,
            RoomType.SUITE,
        )

    @property
    def base_price(self) -> float:
        """Return the base price of the suite room."""

        return 400.0
