"""Tests for the RoomType enum."""

from src.hotel.data.enums.RoomType import RoomType


class TestRoomType:
    """Tests for the RoomType enum."""

    def test_values(self) -> None:
        """Test room type values."""
        assert RoomType.STANDARD.value == "Standard"
        assert RoomType.DELUXE.value == "Deluxe"
        assert RoomType.SUITE.value == "Suite"
        assert RoomType.PENTHOUSE.value == "Penthouse"

    def test_str(self) -> None:
        """Test room type string output."""
        assert str(RoomType.STANDARD) == "Standard"
        assert str(RoomType.DELUXE) == "Deluxe"
        assert str(RoomType.SUITE) == "Suite"
        assert str(RoomType.PENTHOUSE) == "Penthouse"

    def test_repr(self) -> None:
        """Test room type repr output."""
        assert repr(RoomType.STANDARD) == "Standard"
        assert repr(RoomType.DELUXE) == "Deluxe"
        assert repr(RoomType.SUITE) == "Suite"
        assert repr(RoomType.PENTHOUSE) == "Penthouse"

    def test_enum_count(self) -> None:
        """Test total number of room types."""
        assert len(RoomType) == 4
