"""Tests for the Customer class."""

from src.hotel.data.customer.Customer import Customer


class TestCustomer:
    """Tests for the Customer class."""

    def setup_method(self) -> None:
        """Create reusable customer."""
        self.customer = Customer(
            "C001",
            "John Doe",
            "john@email.com",
            "1234567890",
            "123 Main St",
            0.1,
        )

    def test_init(self) -> None:
        """Test customer initialization."""
        assert self.customer.customer_id == "C001"
        assert self.customer.name == "John Doe"
        assert self.customer.email == "john@email.com"
        assert self.customer.phone == "1234567890"
        assert self.customer.address == "123 Main St"
        assert self.customer.discount == 0.1

    def test_default_discount(self) -> None:
        """Test default discount value."""
        customer = Customer(
            "C002",
            "Jane Doe",
            "jane@email.com",
            "9876543210",
            "456 Elm St",
        )

        assert customer.discount == 0.0

    def test_set_name(self) -> None:
        """Test updating customer name."""
        self.customer.name = "Mike"

        assert self.customer.name == "Mike"

    def test_set_email(self) -> None:
        """Test updating customer email."""
        self.customer.email = "new@email.com"

        assert self.customer.email == "new@email.com"

    def test_set_phone(self) -> None:
        """Test updating customer phone."""
        self.customer.phone = "9999999999"

        assert self.customer.phone == "9999999999"

    def test_set_address(self) -> None:
        """Test updating customer address."""
        self.customer.address = "New Address"

        assert self.customer.address == "New Address"

    def test_set_discount(self) -> None:
        """Test updating customer discount."""
        self.customer.discount = 0.25

        assert self.customer.discount == 0.25

    def test_customer_id(self) -> None:
        """Test customer id."""
        assert self.customer.customer_id == "C001"

    def test_str(self) -> None:
        """Test string representation."""
        assert str(self.customer) == "John Doe #C001"
