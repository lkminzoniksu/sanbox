"""Customers panel."""

import tkinter as tk
from tkinter import messagebox

from src.hotel.gui.ParentPanel import ParentPanel


class CustomersPanel(ParentPanel):
    """Panel to display and search customers."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize customers panel."""
        super().__init__(master, controller)

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Customers")

        search_frame = tk.Frame(body, bg=self.background)
        search_frame.pack(fill="x", padx=18, pady=(5, 5))

        search_label = tk.Label(
            search_frame,
            text="Search:",
            bg=self.background,
            fg="black",
        )
        search_label.pack(side="left", padx=(0, 8))

        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 8))

        search_button = self.make_button(
            search_frame,
            "Search",
            self.search_customers,
        )
        search_button.pack(side="left", padx=(0, 8))

        clear_button = self.make_button(
            search_frame,
            "Clear",
            self.clear_search,
        )
        clear_button.pack(side="left")

        card = self.make_card(body)

        columns = ("User ID", "Name", "Phone")
        self.table = self.make_table(card, columns)

        self.load_customers(self._controller.customers)

        button_frame = tk.Frame(body, bg=self.background)
        button_frame.pack(fill="x", padx=18, pady=(0, 16))

        view_button = self.make_button(
            button_frame,
            "View",
            self.view_customer,
        )
        view_button.pack(side="left", padx=(0, 8))

        create_button = self.make_button(
            button_frame,
            "Create",
            lambda: self.load_panel("customer_create"),
        )
        create_button.pack(side="left")

    def load_customers(self, customers) -> None:
        """Load customers into table."""
        for item in self.table.get_children():
            self.table.delete(item)

        for customer in customers:
            values = (
                customer["User ID"],
                customer["Name"],
                customer["Phone"],
            )

            self.table.insert("", "end", values=values)

    def search_customers(self) -> None:
        """Search customers."""
        search_text = self.search_entry.get().lower().strip()
        results = []

        for customer in self._controller.customers:
            customer_id = customer.get("User ID", "").lower()
            name = customer.get("Name", "").lower()
            phone = customer.get("Phone", "").lower()
            email = customer.get("Email", "").lower()

            if (
                search_text in customer_id
                or search_text in name
                or search_text in phone
                or search_text in email
            ):
                results.append(customer)

        self.load_customers(results)

    def clear_search(self) -> None:
        """Clear search and reload all customers."""
        self.search_entry.delete(0, tk.END)
        self.load_customers(self._controller.customers)

    def view_customer(self) -> None:
        """View the selected customer."""
        selected = self.table.selection()

        if len(selected) == 0:
            messagebox.showerror(
                "Error",
                "Please select a customer.",
            )
            return

        values = self.table.item(selected[0], "values")
        customer_id = values[0]

        self.load_panel("customer_view", customer_id)
