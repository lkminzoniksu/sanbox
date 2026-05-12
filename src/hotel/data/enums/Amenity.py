"""Defines the Amenities enumeration for hotel rooms."""
from enum import Enum


class Amenity(Enum):
    """Enumeration representing room amenities."""
    BREAKFAST = "Breakfast"
    PARKING = "Parking"
    POOL = "Pool"
    VIEW = "View"
    EXTRA_BED = "Extra Bed"
    PET_AREA = "Pet Area"
    JACUZZI = "Jacuzzi"
    BALCONY = "Balcony"

    def __str__(self) -> str:
        """Return the string representation of the amenity."""
        return str(self.value)

    def __repr__(self) -> str:
        """Return the official string representation of the amenity."""
        return str(self)
