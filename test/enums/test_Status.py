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
        assert str(Status.PENDING) == "Pending"
        assert str(Status.CONFIRMED) == "Confirmed"
        assert str(Status.CHECKED_IN) == "Checked-in"
        assert str(Status.CHECKED_OUT) == "Checked-out"
        assert str(Status.CANCELLED) == "Cancelled"
        assert str(Status.NO_SHOW) == "No-show"

    def test_repr(self) -> None:
        """Test status repr output."""
        assert repr(Status.PENDING) == "Pending"
        assert repr(Status.CONFIRMED) == "Confirmed"
        assert repr(Status.CHECKED_IN) == "Checked-in"
        assert repr(Status.CHECKED_OUT) == "Checked-out"
        assert repr(Status.CANCELLED) == "Cancelled"
        assert repr(Status.NO_SHOW) == "No-show"

    def test_enum_count(self) -> None:
        """Test total number of statuses."""
        assert len(Status) == 6
