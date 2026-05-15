"""Customer create panel."""

import tkinter as tk
from tkinter import messagebox

from src.hotel.gui.ParentPanel import ParentPanel


class CustomerCreatePanel(ParentPanel):
    """Panel to create a new customer."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize customer create panel."""
        super().__init__(master, controller)

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Customers / Create")

        card = self.make_card(body)

        title = tk.Label(
            card,
            text="Create Customer",
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 20, "bold"),
        )
        title.pack(pady=(30, 20))

        form = tk.Frame(card, bg=self.panel_bg)
        form.pack(fill="x", padx=80, pady=10)

        self.name_entry = self.make_entry_row(form, "Name:")
        self.phone_entry = self.make_entry_row(form, "Phone:")
        self.email_entry = self.make_entry_row(form, "Email:")
        self.address_entry = self.make_entry_row(form, "Address:")

        button_frame = tk.Frame(card, bg=self.panel_bg)
        button_frame.pack(fill="x", padx=80, pady=20)

        save_button = self.make_button(
            button_frame,
            "Save",
            self.save_customer,
        )
        save_button.pack(side="left", padx=(0, 8))

        cancel_button = self.make_button(
            button_frame,
            "Cancel",
            lambda: self.load_panel("customers"),
        )
        cancel_button.pack(side="left")

    def save_customer(self) -> None:
        """Save a new customer in memory and JSON."""
        if self.name_entry.get().strip() == "":
            messagebox.showerror(
                "Error",
                "Customer name is required.",
            )
            return

        new_id = str(1000 + len(self._controller.customers) + 1)

        customer = {
            "User ID": new_id,
            "Name": self.name_entry.get(),
            "Phone": self.phone_entry.get(),
            "Email": self.email_entry.get(),
            "Address": self.address_entry.get(),
        }

        self._controller.customers.append(customer)
        self._controller.save_customers()

        self.load_panel("customers")
