"""Tests for reservation logic."""

from datetime import datetime


def calculate_nights(
    checkin: str,
    checkout: str,
) -> int:
    """Calculate nights between two dates."""
    date_in = datetime.strptime(
        checkin,
        "%m/%d/%Y",
    )

    date_out = datetime.strptime(
        checkout,
        "%m/%d/%Y",
    )

    return (date_out - date_in).days


def dates_overlap(
    new_checkin: str,
    new_checkout: str,
    old_checkin: str,
    old_checkout: str,
) -> bool:
    """Return whether two reservation date ranges overlap."""
    new_in = datetime.strptime(
        new_checkin,
        "%m/%d/%Y",
    )

    new_out = datetime.strptime(
        new_checkout,
        "%m/%d/%Y",
    )

    old_in = datetime.strptime(
        old_checkin,
        "%m/%d/%Y",
    )

    old_out = datetime.strptime(
        old_checkout,
        "%m/%d/%Y",
    )

    return new_in < old_out and new_out > old_in


def get_room_rate(room_type: str) -> float:
    """Return room rate by room type."""
    if room_type == "Standard":
        return 200.0

    if room_type == "Deluxe":
        return 300.0

    if room_type == "Suite":
        return 400.0

    if room_type == "Penthouse":
        return 500.0

    return 0.0


def calculate_tax(subtotal: float) -> float:
    """Calculate invoice tax."""
    return subtotal * 0.085


def calculate_total(
    subtotal: float,
    tax: float,
) -> float:
    """Calculate invoice total."""
    return subtotal + tax


def test_calculate_nights() -> None:
    """Test nights calculation."""
    assert calculate_nights(
        "05/12/2026",
        "05/15/2026",
    ) == 3


def test_dates_overlap_true() -> None:
    """Test overlapping dates."""
    assert dates_overlap(
        "05/14/2026",
        "05/17/2026",
        "05/12/2026",
        "05/15/2026",
    )


def test_dates_overlap_false() -> None:
    """Test non-overlapping dates."""
    assert not dates_overlap(
        "05/16/2026",
        "05/18/2026",
        "05/12/2026",
        "05/15/2026",
    )


def test_dates_touching_do_not_overlap() -> None:
    """Test checkout and checkin on same day do not overlap."""
    assert not dates_overlap(
        "05/15/2026",
        "05/18/2026",
        "05/12/2026",
        "05/15/2026",
    )


def test_standard_room_subtotal() -> None:
    """Test standard room subtotal."""
    nights = calculate_nights(
        "05/12/2026",
        "05/15/2026",
    )

    subtotal = nights * get_room_rate("Standard")

    assert subtotal == 600.0


def test_deluxe_room_subtotal() -> None:
    """Test deluxe room subtotal."""
    nights = calculate_nights(
        "05/12/2026",
        "05/15/2026",
    )

    subtotal = nights * get_room_rate("Deluxe")

    assert subtotal == 900.0


def test_suite_room_subtotal() -> None:
    """Test suite room subtotal."""
    nights = calculate_nights(
        "05/12/2026",
        "05/15/2026",
    )

    subtotal = nights * get_room_rate("Suite")

    assert subtotal == 1200.0


def test_penthouse_room_subtotal() -> None:
    """Test penthouse room subtotal."""
    nights = calculate_nights(
        "05/12/2026",
        "05/14/2026",
    )

    subtotal = nights * get_room_rate("Penthouse")

    assert subtotal == 1000.0


def test_tax_calculation() -> None:
    """Test tax calculation."""
    assert calculate_tax(1000.0) == 85.0


def test_total_calculation() -> None:
    """Test total calculation."""
    assert calculate_total(
        1000.0,
        85.0,
    ) == 1085.0
