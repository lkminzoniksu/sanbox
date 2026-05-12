"""Book room panel for hotel GUI."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel
from src.hotel.data.room.StandardRoom import StandardRoom
from src.hotel.data.room.DeluxeRoom import DeluxeRoom
from src.hotel.data.room.SuiteRoom import SuiteRoom
from src.hotel.data.room.PenthouseRoom import PenthouseRoom
from src.hotel.data.enums.BedType import BedType


class BookRoomPanel(ParentPanel):
    """Panel for booking a hotel room."""

    def __init__(self, master, controller) -> None:
        """Initialize the book room panel."""
        super().__init__(master, controller)

        title = tk.Label(self, text="Book Room", font=("Arial", 20))
        title.pack(pady=10)

        return_button = tk.Button(
            self,
            text="Return",
            command=lambda: self.load_panel("home")
        )
        return_button.pack(pady=5)

        customer_label = tk.Label(self, text="Customer Name:")
        customer_label.pack()

        self.customer_entry = tk.Entry(self)
        self.customer_entry.pack(pady=5)

        room_label = tk.Label(self, text="Room Number:")
        room_label.pack()

        self.room_entry = tk.Entry(self)
        self.room_entry.pack(pady=5)

        nights_label = tk.Label(self, text="Number of Nights:")
        nights_label.pack()

        self.nights_entry = tk.Entry(self)
        self.nights_entry.pack(pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

        calculate_button = tk.Button(
            self,
            text="Calculate Total",
            command=self.calculate_total
        )
        calculate_button.pack(pady=5)

        book_button = tk.Button(
            self,
            text="Book Room",
            command=self.book_room
        )
        book_button.pack(pady=5)

    def calculate_total(self) -> None:
        """Calculate total price based on room type."""
        try:
            room_number = int(self.room_entry.get())
            nights = int(self.nights_entry.get())

            # simple rule based on room number
            if room_number < 200:
                room = StandardRoom(room_number, BedType.QUEEN, False)
            elif room_number < 300:
                room = DeluxeRoom(room_number, BedType.KING, False)
            elif room_number < 400:
                room = SuiteRoom(room_number, BedType.KING, False)
            else:
                room = PenthouseRoom(room_number, BedType.KING, False)

            total = room.calculate_price(nights)

            self.result_label.config(
                text=f"Estimated Total: ${total:.2f} ({room.room_type})"
            )

        except ValueError:
            self.result_label.config(text="Invalid input.")

    def book_room(self) -> None:
        """Display booking confirmation."""
        customer = self.customer_entry.get()
        room = self.room_entry.get()
        nights = self.nights_entry.get()

        if customer == "" or room == "" or nights == "":
            self.result_label.config(text="Please fill all fields.")
        else:
            self.result_label.config(
                text=(
                    f"Room {room} booked for {customer} "
                    f"for {nights} nights."
                )
            )
