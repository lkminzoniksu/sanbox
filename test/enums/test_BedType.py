"""Tests for the BedType enum."""

from src.hotel.data.enums.BedType import BedType


class TestBedType:
    """Tests for the BedType enum."""

    def test_values(self) -> None:
        """Test bed type values."""
        assert BedType.TWIN.value == "Twin"
        assert BedType.QUEEN.value == "Queen"
        assert BedType.KING.value == "King"

    def test_str(self) -> None:
        """Test bed type string output."""
        assert str(BedType.QUEEN) == "Queen"

    def test_repr(self) -> None:
        """Test bed type repr output."""
        assert repr(BedType.KING) == "King"
