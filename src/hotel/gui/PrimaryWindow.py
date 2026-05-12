"""Primary window for hotel GUI."""

import tkinter as tk

from src.hotel.gui.HomePanel import HomePanel
from src.hotel.gui.RoomsPanel import RoomsPanel
from src.hotel.gui.CustomersPanel import CustomersPanel
from src.hotel.gui.ReservationsPanel import ReservationsPanel
from src.hotel.gui.BookRoomPanel import BookRoomPanel


class PrimaryWindow(tk.Tk):
    """Main application window for the hotel system."""

    def __init__(self) -> None:
        """Initialize the primary window."""
        super().__init__()

        self.title("Hotel PieCharm")
        self.geometry("700x500")

        self._current_panel = None
        self.load_panel("home")

    def load_panel(self, panel_name: str) -> None:
        """Load the selected panel."""
        if self._current_panel is not None:
            self._current_panel.destroy()

        if panel_name == "home":
            self._current_panel = HomePanel(self, self)

        elif panel_name == "rooms":
            self._current_panel = RoomsPanel(self, self)

        elif panel_name == "customers":
            self._current_panel = CustomersPanel(self, self)

        elif panel_name == "reservations":
            self._current_panel = ReservationsPanel(self, self)

        elif panel_name == "book":
            self._current_panel = BookRoomPanel(self, self)

        else:
            self._current_panel = HomePanel(self, self)

        self._current_panel.pack(fill="both", expand=True)
