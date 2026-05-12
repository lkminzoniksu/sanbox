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
        assert str(RoomType.DELUXE) == "Deluxe"

    def test_repr(self) -> None:
        """Test room type repr output."""
        assert repr(RoomType.SUITE) == "Suite"
