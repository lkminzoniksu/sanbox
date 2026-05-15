"""GUI panel for displaying reservation invoices."""

import tkinter as tk
from datetime import datetime

from src.hotel.gui.ParentPanel import ParentPanel


class InvoicePanel(ParentPanel):
    """GUI panel for displaying a completed invoice."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize the invoice panel."""
        super().__init__(master, controller)

        self.item_id = item_id
        self.reservation = self.find_reservation()

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Invoice")

        card = self.make_card(body)

        title = tk.Label(
            card,
            text="Hotel PieCharm Invoice",
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 22, "bold"),
        )
        title.pack(pady=(25, 15))

        invoice_text = self.build_invoice()

        invoice_label = tk.Label(
            card,
            text=invoice_text,
            bg="white",
            fg="black",
            font=("Courier New", 12),
            justify="left",
            anchor="w",
            relief="solid",
            bd=1,
            padx=20,
            pady=20,
        )
        invoice_label.pack(fill="both", expand=True, padx=80, pady=10)

        button_frame = tk.Frame(card, bg=self.panel_bg)
        button_frame.pack(fill="x", padx=80, pady=20)

        return_button = self.make_button(
            button_frame,
            "Return",
            lambda: self.load_panel("reservations"),
        )
        return_button.pack(side="left")

    def find_reservation(self) -> dict:
        """Return the reservation matching the selected id."""
        for reservation in self._controller.reservations:
            if reservation.get("Res ID", "") == self.item_id:
                return reservation

        return {
            "Res ID": "",
            "Guest": "",
            "Room": "",
            "Date in": "",
            "Check-out": "",
            "Amenities": "",
            "Total": "$0.00",
            "Status": "",
        }

    def calculate_nights(self, checkin: str, checkout: str) -> int:
        """Return the number of nights between two dates."""
        try:
            date_in = datetime.strptime(checkin, "%m/%d/%Y")
            date_out = datetime.strptime(checkout, "%m/%d/%Y")
            nights = (date_out - date_in).days

            if nights <= 0:
                return 1

            return nights

        except ValueError:
            return 1

    def get_room_rate(self, room_number: str) -> float:
        """Return the nightly rate for the reservation room."""
        for room in self._controller.rooms:
            if room.get("Room", "") == room_number:
                room_type = room.get("Type", "")

                if room_type == "Standard":
                    return 200.00

                if room_type == "Deluxe":
                    return 300.00

                if room_type == "Suite":
                    return 400.00

                if room_type == "Penthouse":
                    return 500.00

        return 200.00

    def build_invoice(self) -> str:
        """Create invoice text for the reservation."""
        checkin = self.reservation.get("Date in", "")
        checkout = self.reservation.get("Check-out", "")
        room_number = self.reservation.get("Room", "")

        nights = self.calculate_nights(checkin, checkout)
        rate = self.get_room_rate(room_number)
        subtotal = nights * rate
        tax = subtotal * 0.085
        total = subtotal + tax

        self.reservation["Total"] = f"${total:.2f}"
        self._controller.save_reservations()

        return (
            "HOTEL PIECHARM\n"
            "------------------------------\n"
            f"Reservation ID: {self.reservation.get('Res ID', '')}\n"
            f"Guest:          {self.reservation.get('Guest', '')}\n"
            f"Room:           {room_number}\n"
            f"Check-in:       {checkin}\n"
            f"Check-out:      {checkout}\n"
            f"Nights:         {nights}\n"
            f"Rate/Night:     ${rate:.2f}\n"
            f"Amenities:      {self.reservation.get('Amenities', '')}\n"
            "------------------------------\n"
            f"Subtotal:       ${subtotal:.2f}\n"
            f"Tax:            ${tax:.2f}\n"
            f"Total:          ${total:.2f}\n"
            "------------------------------\n"
            "Status:         Checked-out"
        )
