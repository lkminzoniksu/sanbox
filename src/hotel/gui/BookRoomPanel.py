"""Book room panel."""

import tkinter as tk
from tkinter import ttk

from src.hotel.gui.ParentPanel import ParentPanel


class BookRoomPanel(ParentPanel):
    """Panel to create a room reservation."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize book room panel."""
        super().__init__(master, controller)

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Reservations / New")

        card = self.make_card(body)

        form = tk.Frame(card, bg=self.panel_bg)
        form.pack(fill="x", padx=20, pady=20)

        self.guest_entry = self.make_entry_row(
            form,
            "Guest:",
            "John Doe")
        self.email_entry = self.make_entry_row(
            form,
            "Email:",
            "John.Doe@news.com")
        self.phone_entry = self.make_entry_row(
            form,
            "Phone:",
            "(785) 223-2222")

        room_row = tk.Frame(form, bg=self.panel_bg)
        room_row.pack(fill="x", pady=5)

        room_label = tk.Label(
            room_row,
            text="Room:",
            bg=self.panel_bg,
            width=12,
            anchor="w",
        )
        room_label.pack(side="left")
        self.room_combo = ttk.Combobox(
            room_row,
            values=[
                "101",
                "102",
                "105",
                "201",
                "202",
                "203"],
            state="readonly",
        )
        self.room_combo.set("101")
        self.room_combo.pack(side="left", fill="x", expand=True)

        self.checkin_entry = self.make_entry_row(
            form,
            "Check-in:",
            "02/22/2022")
        self.checkout_entry = self.make_entry_row(
            form,
            "Check-out:",
            "02/25/2022")
        self.total_entry = self.make_entry_row(
            form,
            "Total:",
            "$350.00")

        button_frame = tk.Frame(card, bg=self.panel_bg)
        button_frame.pack(fill="x", padx=20, pady=10)

        confirm_button = self.make_button(
            button_frame,
            "Confirm",
            self.create_reservation,
        )
        confirm_button.pack(side="left", padx=(0, 8))

        cancel_button = self.make_button(
            button_frame,
            "Cancel",
            lambda: self.load_panel("home"),
        )
        cancel_button.pack(side="left")

    def create_reservation(self) -> None:
        """Create a reservation in memory."""
        new_id = str(1000 + len(self._controller.reservations) + 1)

        reservation = {
            "Res ID": new_id,
            "Type": "std",
            "Date in": self.checkin_entry.get(),
            "Paid": "No",
            "Status": "Conf",
            "Guest": self.guest_entry.get(),
        }

        self._controller.reservations.append(reservation)
        self.load_panel("reservations")
