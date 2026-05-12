"""Tests for the Customer class."""

from src.hotel.data.customer.Customer import Customer


class TestCustomer:
    """Tests for the Customer class."""

    def test_init(self) -> None:
        """Test customer initialization."""
        customer = Customer(
            "C001",
            "John Doe",
            "john@email.com",
            "1234567890",
            "123 Main St",
            0.1
        )

        assert customer.customer_id == "C001"
        assert customer.name == "John Doe"
        assert customer.email == "john@email.com"
        assert customer.phone == "1234567890"
        assert customer.address == "123 Main St"
        assert customer.discount == 0.1

    def test_default_discount(self) -> None:
        """Test default discount value."""
        customer = Customer(
            "C002",
            "Jane Doe",
            "jane@email.com",
            "9876543210",
            "456 Elm St"
        )

        assert customer.discount == 0.0

    def test_set_name(self) -> None:
        """Test updating customer name."""
        customer = Customer("C001", "John", "a", "b", "c")
        customer.name = "Mike"
        assert customer.name == "Mike"

    def test_set_email(self) -> None:
        """Test updating customer email."""
        customer = Customer("C001", "John", "a", "b", "c")
        customer.email = "new@email.com"
        assert customer.email == "new@email.com"

    def test_set_phone(self) -> None:
        """Test updating customer phone."""
        customer = Customer("C001", "John", "a", "b", "c")
        customer.phone = "9999999999"
        assert customer.phone == "9999999999"

    def test_set_address(self) -> None:
        """Test updating customer address."""
        customer = Customer("C001", "John", "a", "b", "c")
        customer.address = "New Address"
        assert customer.address == "New Address"

    def test_str(self) -> None:
        """Test string representation."""
        customer = Customer(
            "C001",
            "John Doe",
            "a",
            "b",
            "c"
        )

        assert str(customer) == "John Doe #C001"
