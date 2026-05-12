"""Rooms panel for hotel GUI."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel


class RoomsPanel(ParentPanel):
    """Panel that displays hotel rooms."""

    def __init__(self, master, controller) -> None:
        """Initialize the rooms panel."""
        super().__init__(master, controller)

        title = tk.Label(self, text="Rooms", font=("Arial", 20))
        title.pack(pady=10)

        return_button = tk.Button(
            self,
            text="Return",
            command=lambda: self.load_panel("home")
        )
        return_button.pack(pady=5)

        header = tk.Label(
            self,
            text="Room      Type      Bed      Smoking      Status"
        )
        header.pack(pady=5)

        rooms = [
            "101       Standard  Queen    No           Free",
            "102       Deluxe    King     Yes          Free",
            "301       Suite     King     No           Free",
        ]

        for room in rooms:
            label = tk.Label(self, text=room)
            label.pack()

        check_in_button = tk.Button(self, text="Check-in")
        check_in_button.pack(pady=5)

        check_out_button = tk.Button(self, text="Check-out")
        check_out_button.pack(pady=5)
