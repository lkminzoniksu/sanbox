"""Customer class for the hotel system."""


class Customer:
    """Represents a hotel customer."""
    def __init__(
        self,
        customer_id: str,
        name: str,
        email: str,
        phone: str,
        address: str,
        discount: float = 0.0
    ) -> None:
        """Initialize a customer with basic attributes."""
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone = phone
        self._address = address
        self._discount = discount

    @property
    def customer_id(self) -> str:
        """Return the customer id."""
        return self._customer_id

    @property
    def name(self) -> str:
        """Return the customer name."""
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """Update the customer name."""
        self._name = name

    @property
    def email(self) -> str:
        """Return the customer email."""
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """Update the customer email."""
        self._email = email

    @property
    def phone(self) -> str:
        """Return the customer phone."""
        return self._phone

    @phone.setter
    def phone(self, phone: str) -> None:
        """Update the customer phone."""
        self._phone = phone

    @property
    def address(self) -> str:
        """Return the customer address."""
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """Update the customer address."""
        self._address = address

    @property
    def discount(self) -> float:
        """Return the customer given discount."""
        return self._discount

    @discount.setter
    def discount(self, value: float) -> None:
        """Set customer discount."""
        self._discount = value

    def __str__(self) -> str:
        """Return the string representation of the customer."""
        return f"{self._name} #{self._customer_id}"
