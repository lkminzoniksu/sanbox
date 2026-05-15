"""Customer view panel."""

import tkinter as tk
from tkinter import messagebox

from src.hotel.gui.ParentPanel import ParentPanel


class CustomerViewPanel(ParentPanel):
    """Panel to view and edit a customer."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize customer view panel."""
        super().__init__(master, controller)

        self.item_id = item_id
        self.customer = self.find_customer()

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Customers / View")

        card = self.make_card(body)

        title = tk.Label(
            card,
            text="View Customer",
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 20, "bold"),
        )
        title.pack(pady=(30, 20))

        form = tk.Frame(card, bg=self.panel_bg)
        form.pack(fill="x", padx=80, pady=10)

        self.id_entry = self.make_entry_row(
            form,
            "User ID:",
            self.customer["User ID"],
        )
        self.name_entry = self.make_entry_row(
            form,
            "Name:",
            self.customer["Name"],
        )
        self.phone_entry = self.make_entry_row(
            form,
            "Phone:",
            self.customer["Phone"],
        )
        self.email_entry = self.make_entry_row(
            form,
            "Email:",
            self.customer.get("Email", ""),
        )
        self.address_entry = self.make_entry_row(
            form,
            "Address:",
            self.customer.get("Address", ""),
        )

        self.disable_entries()

        button_frame = tk.Frame(card, bg=self.panel_bg)
        button_frame.pack(fill="x", padx=80, pady=20)

        self.edit_button = self.make_button(
            button_frame,
            "Edit",
            self.enable_edit,
        )
        self.edit_button.pack(side="left", padx=(0, 8))

        self.save_button = self.make_button(
            button_frame,
            "Save",
            self.save_customer,
        )
        self.save_button.pack(side="left", padx=(0, 8))
        self.save_button.config(state="disabled")

        book_button = self.make_button(
            button_frame,
            "Create Reservation",
            lambda: self.load_panel(
                "reservation_create",
                self.customer["User ID"],
            ),
        )
        book_button.pack(side="left", padx=(0, 8))

        delete_button = self.make_button(
            button_frame,
            "Delete",
            self.delete_customer,
        )
        delete_button.pack(side="left", padx=(0, 8))

        return_button = self.make_button(
            button_frame,
            "Return",
            lambda: self.load_panel("customers"),
        )
        return_button.pack(side="left")

    def find_customer(self) -> dict:
        """Find customer by id."""
        for customer in self._controller.customers:
            if customer["User ID"] == self.item_id:
                return customer

        if len(self._controller.customers) > 0:
            return self._controller.customers[0]

        return {
            "User ID": "",
            "Name": "",
            "Phone": "",
            "Email": "",
            "Address": "",
        }

    def disable_entries(self) -> None:
        """Disable entry fields but keep text readable."""
        entries = [
            self.id_entry,
            self.name_entry,
            self.phone_entry,
            self.email_entry,
            self.address_entry,
        ]

        for entry in entries:
            entry.config(
                state="readonly",
                readonlybackground="white",
                fg="black",
            )

    def enable_edit(self) -> None:
        """Enable editing for customer fields."""
        self.name_entry.config(state="normal", fg="black")
        self.phone_entry.config(state="normal", fg="black")
        self.email_entry.config(state="normal", fg="black")
        self.address_entry.config(state="normal", fg="black")

        self.edit_button.config(state="disabled")
        self.save_button.config(state="normal")

    def save_customer(self) -> None:
        """Save customer changes."""
        if self.name_entry.get().strip() == "":
            messagebox.showerror(
                "Error",
                "Customer name is required.",
            )
            return

        self.customer["Name"] = self.name_entry.get()
        self.customer["Phone"] = self.phone_entry.get()
        self.customer["Email"] = self.email_entry.get()
        self.customer["Address"] = self.address_entry.get()

        self._controller.save_customers()

        self.load_panel("customers")

    def delete_customer(self) -> None:
        """Delete customer."""
        answer = messagebox.askyesno(
            "Delete Customer",
            "Are you sure you want to delete this customer?",
        )

        if not answer:
            return

        if self.customer in self._controller.customers:
            self._controller.customers.remove(self.customer)

        self._controller.save_customers()

        messagebox.showinfo(
            "Success",
            "Customer deleted.",
        )

        self.load_panel("customers")
