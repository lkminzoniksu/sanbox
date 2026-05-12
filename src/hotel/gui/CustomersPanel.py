"""Customers panel for hotel GUI."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel


class CustomersPanel(ParentPanel):
    """Panel that displays hotel customers."""

    def __init__(self, master, controller) -> None:
        """Initialize the customers panel."""
        super().__init__(master, controller)

        title = tk.Label(self, text="Customers", font=("Arial", 20))
        title.pack(pady=10)

        return_button = tk.Button(
            self,
            text="Return",
            command=lambda: self.load_panel("home")
        )
        return_button.pack(pady=5)

        header = tk.Label(
            self,
            text="ID        Name              Email"
        )
        header.pack(pady=5)

        customers = [
            "C001      John Doe          john@email.com",
            "C002      Jane Smith        jane@email.com",
            "C003      Lucas Minzoni     lucas@email.com",
        ]

        for customer in customers:
            label = tk.Label(self, text=customer)
            label.pack()

        add_button = tk.Button(self, text="Add Customer")
        add_button.pack(pady=10)

        edit_button = tk.Button(self, text="Edit Customer")
        edit_button.pack(pady=10)
