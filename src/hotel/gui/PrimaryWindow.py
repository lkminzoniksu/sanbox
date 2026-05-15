"""Primary window for hotel GUI."""

import json
import tkinter as tk

from src.hotel.gui.BookRoomPanel import BookRoomPanel
from src.hotel.gui.CustomerCreatePanel import CustomerCreatePanel
from src.hotel.gui.CustomerViewPanel import CustomerViewPanel
from src.hotel.gui.CustomersPanel import CustomersPanel
from src.hotel.gui.HomePanel import HomePanel
from src.hotel.gui.ReportsPanel import ReportsPanel
from src.hotel.gui.ReservationCreatePanel import ReservationCreatePanel
from src.hotel.gui.ReservationViewPanel import ReservationViewPanel
from src.hotel.gui.ReservationsPanel import ReservationsPanel
from src.hotel.gui.RoomsPanel import RoomsPanel
from src.hotel.gui.InvoicePanel import InvoicePanel


class PrimaryWindow(tk.Tk):
    """Main application window for the hotel system."""

    def __init__(self) -> None:
        """Initialize the primary window."""
        super().__init__()

        self.title("Hotel PieCharm")
        self.geometry("1000x650")
        self.minsize(900, 580)
        self.configure(bg="#f7f3fb")

        self.rooms = [
            {
                "Room": "101",
                "Type": "std",
                "Bed": "Q",
                "Smoking": "No",
                "Status": "Free",
            },
            {
                "Room": "102",
                "Type": "std",
                "Bed": "Q",
                "Smoking": "Yes",
                "Status": "Free",
            },
            {
                "Room": "105",
                "Type": "std",
                "Bed": "Q",
                "Smoking": "No",
                "Status": "Free",
            },
            {
                "Room": "201",
                "Type": "dlx",
                "Bed": "K",
                "Smoking": "No",
                "Status": "Free",
            },
            {
                "Room": "202",
                "Type": "dlx",
                "Bed": "Q",
                "Smoking": "No",
                "Status": "Free",
            },
            {
                "Room": "203",
                "Type": "ste",
                "Bed": "K",
                "Smoking": "No",
                "Status": "Free",
            },
        ]

        self.customers = [
            {
                "User ID": "1234",
                "Name": "John Doe",
                "Phone": "(785)222-2344",
                "Email": "John.Doe@news.com",
                "Address": "",
            }
        ]

        self.reservations: list = []

        self.load_rooms()
        self.load_customers()
        self.load_reservations()

        self._current_panel: tk.Frame | None = None
        self.load_panel("home")

    def load_rooms(self) -> None:
        """Load rooms from JSON file."""
        try:
            with open("rooms.json", "r", encoding="utf-8") as file:
                self.rooms = json.load(file)
        except FileNotFoundError:
            self.save_rooms()

    def save_rooms(self) -> None:
        """Save rooms to JSON file."""
        with open("rooms.json", "w", encoding="utf-8") as file:
            json.dump(self.rooms, file, indent=4)

    def load_customers(self) -> None:
        """Load customers from JSON file."""
        try:
            with open("customers.json", "r", encoding="utf-8") as file:
                self.customers = json.load(file)
        except FileNotFoundError:
            self.save_customers()

    def save_customers(self) -> None:
        """Save customers to JSON file."""
        with open("customers.json", "w", encoding="utf-8") as file:
            json.dump(self.customers, file, indent=4)

    def load_reservations(self) -> None:
        """Load reservations from JSON file."""
        try:
            with open("reservations.json", "r", encoding="utf-8") as file:
                self.reservations = json.load(file)
        except FileNotFoundError:
            self.save_reservations()

    def save_reservations(self) -> None:
        """Save reservations to JSON file."""
        with open("reservations.json", "w", encoding="utf-8") as file:
            json.dump(self.reservations, file, indent=4)

    def load_panel(self, panel_name: str, item_id: str = "") -> None:
        """Load the selected panel."""
        if self._current_panel is not None:
            self._current_panel.destroy()

        panels = {
            "home": HomePanel,
            "rooms": RoomsPanel,
            "customers": CustomersPanel,
            "customer_create": CustomerCreatePanel,
            "customer_view": CustomerViewPanel,
            "reservations": ReservationsPanel,
            "reservation_create": ReservationCreatePanel,
            "reservation_view": ReservationViewPanel,
            "book": BookRoomPanel,
            "reports": ReportsPanel,
            "invoice": InvoicePanel,
        }

        panel_class = panels.get(panel_name, HomePanel)
        self._current_panel = panel_class(self, self, item_id)
        self._current_panel.pack(fill="both", expand=True)
