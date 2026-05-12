"""Tests for the Status enum."""

from src.hotel.data.enums.Status import Status


class TestStatus:
    """Tests for the Status enum."""

    def test_values(self) -> None:
        """Test status values."""
        assert Status.PENDING.value == "Pending"
        assert Status.CONFIRMED.value == "Confirmed"
        assert Status.CHECKED_IN.value == "Checked-in"
        assert Status.CHECKED_OUT.value == "Checked-out"
        assert Status.CANCELLED.value == "Cancelled"
        assert Status.NO_SHOW.value == "No-show"

    def test_str(self) -> None:
        """Test status string output."""
        assert str(Status.CHECKED_IN) == "Checked-in"

    def test_repr(self) -> None:
        """Test status repr output."""
        assert repr(Status.CANCELLED) == "Cancelled"
