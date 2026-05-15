"""Reservations panel."""

import tkinter as tk
from tkinter import messagebox

from src.hotel.gui.ParentPanel import ParentPanel


class ReservationsPanel(ParentPanel):
    """Panel to display and search reservations."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize reservations panel."""
        super().__init__(master, controller)

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Reservations")

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
            self.search_reservations,
        )
        search_button.pack(side="left", padx=(0, 8))

        clear_button = self.make_button(
            search_frame,
            "Clear",
            self.clear_search,
        )
        clear_button.pack(side="left")

        card = self.make_card(body)

        columns = (
            "Res ID",
            "Guest",
            "Room",
            "Date in",
            "Check-out",
            "Status",
        )

        self.table = self.make_table(card, columns)

        self.load_reservations(self._controller.reservations)

        button_frame = tk.Frame(body, bg=self.background)
        button_frame.pack(fill="x", padx=18, pady=(0, 16))

        view_button = self.make_button(
            button_frame,
            "View",
            self.view_reservation,
        )
        view_button.pack(side="left", padx=(0, 8))

        create_button = self.make_button(
            button_frame,
            "Create",
            lambda: self.load_panel("reservation_create"),
        )
        create_button.pack(side="left")

    def load_reservations(self, reservations) -> None:
        """Load reservations into table."""
        for item in self.table.get_children():
            self.table.delete(item)

        for reservation in reservations:
            values = (
                reservation.get("Res ID", ""),
                reservation.get("Guest", ""),
                reservation.get("Room", ""),
                reservation.get("Date in", ""),
                reservation.get("Check-out", ""),
                reservation.get("Status", ""),
            )

            self.table.insert("", "end", values=values)

    def search_reservations(self) -> None:
        """Search reservations by ID, user, room, or date."""
        search_text = self.search_entry.get().lower().strip()
        results = []

        for reservation in self._controller.reservations:
            reservation_id = reservation.get("Res ID", "").lower()
            guest = reservation.get("Guest", "").lower()
            room = reservation.get("Room", "").lower()
            date_in = reservation.get("Date in", "").lower()
            date_out = reservation.get("Check-out", "").lower()

            if (
                search_text in reservation_id
                or search_text in guest
                or search_text in room
                or search_text in date_in
                or search_text in date_out
            ):
                results.append(reservation)

        self.load_reservations(results)

    def clear_search(self) -> None:
        """Clear search and reload all reservations."""
        self.search_entry.delete(0, tk.END)
        self.load_reservations(self._controller.reservations)

    def view_reservation(self) -> None:
        """Open selected reservation."""
        selected = self.table.selection()

        if len(selected) == 0:
            messagebox.showerror(
                "Error",
                "Please select a reservation.",
            )
            return

        values = self.table.item(selected[0], "values")
        reservation_id = values[0]

        self.load_panel("reservation_view", reservation_id)
