"""Reservations panel for hotel GUI."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel


class ReservationsPanel(ParentPanel):
    """Panel that displays hotel reservations."""

    def __init__(self, master, controller) -> None:
        """Initialize the reservations panel."""
        super().__init__(master, controller)

        title = tk.Label(self, text="Reservations", font=("Arial", 20))
        title.pack(pady=10)

        return_button = tk.Button(
            self,
            text="Return",
            command=lambda: self.load_panel("home")
        )
        return_button.pack(pady=5)

        header = tk.Label(
            self,
            text="ID        Guest          Room      Status"
        )
        header.pack(pady=5)

        reservations = [
            "R001      John Doe       101       Pending",
            "R002      Jane Smith     201       Confirmed",
            "R003      Lucas          301       Checked-in",
        ]

        for reservation in reservations:
            label = tk.Label(self, text=reservation)
            label.pack()

        cancel_button = tk.Button(self, text="Cancel Reservation")
        cancel_button.pack(pady=10)
