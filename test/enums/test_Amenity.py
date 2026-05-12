"""Tests for the Amenity enum."""

from src.hotel.data.enums.Amenity import Amenity


class TestAmenity:
    """Tests for the Amenity enum."""

    def test_values(self) -> None:
        """Test amenity values."""
        assert Amenity.BREAKFAST.value == "Breakfast"
        assert Amenity.PARKING.value == "Parking"
        assert Amenity.POOL.value == "Pool"
        assert Amenity.VIEW.value == "View"
        assert Amenity.EXTRA_BED.value == "Extra Bed"
        assert Amenity.PET_AREA.value == "Pet Area"
        assert Amenity.JACUZZI.value == "Jacuzzi"
        assert Amenity.BALCONY.value == "Balcony"

    def test_str(self) -> None:
        """Test amenity string output."""
        assert str(Amenity.BREAKFAST) == "Breakfast"

    def test_repr(self) -> None:
        """Test amenity repr output."""
        assert repr(Amenity.POOL) == "Pool"
