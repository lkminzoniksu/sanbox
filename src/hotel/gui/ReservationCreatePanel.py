"""Reservation create panel."""

import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.gui.ParentPanel import ParentPanel


class ReservationCreatePanel(ParentPanel):
    """Panel to create reservations."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize reservation create panel."""
        super().__init__(master, controller)

        self.item_id = item_id
        self.customer = self.find_customer()

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Reservations / New")

        card = self.make_card(body)

        title = tk.Label(
            card,
            text="Create Reservation",
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 20, "bold"),
        )
        title.pack(pady=(30, 20))

        form = tk.Frame(card, bg=self.panel_bg)
        form.pack(fill="x", padx=80, pady=10)

        self.guest_entry = self.make_entry_row(
            form,
            "Guest:",
            self.customer.get("Name", ""),
        )

        self.email_entry = self.make_entry_row(
            form,
            "Email:",
            self.customer.get("Email", ""),
        )

        self.phone_entry = self.make_entry_row(
            form,
            "Phone:",
            self.customer.get("Phone", ""),
        )

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

        room_numbers = []

        for room in self._controller.rooms:
            room_numbers.append(room["Room"])

        self.room_combo = ttk.Combobox(
            room_row,
            values=room_numbers,
            state="readonly",
        )

        if len(room_numbers) > 0:
            self.room_combo.set(room_numbers[0])

        self.room_combo.pack(
            side="left",
            fill="x",
            expand=True,
        )

        amenity_row = tk.Frame(form, bg=self.panel_bg)
        amenity_row.pack(fill="x", pady=5)

        amenity_label = tk.Label(
            amenity_row,
            text="Amenities:",
            bg=self.panel_bg,
            width=12,
            anchor="nw",
        )
        amenity_label.pack(side="left", pady=4)

        self.amenity_listbox = tk.Listbox(
            amenity_row,
            selectmode=tk.MULTIPLE,
            height=6,
            exportselection=False,
        )

        for amenity in Amenity:
            self.amenity_listbox.insert(
                tk.END,
                amenity.value,
            )

        self.amenity_listbox.pack(
            side="left",
            fill="x",
            expand=True,
        )

        self.checkin_entry = self.make_entry_row(
            form,
            "Check-in:",
            "05/12/2026",
        )

        self.checkout_entry = self.make_entry_row(
            form,
            "Check-out:",
            "05/15/2026",
        )

        self.total_entry = self.make_entry_row(
            form,
            "Total:",
            "$350.00",
        )

        button_frame = tk.Frame(card, bg=self.panel_bg)
        button_frame.pack(fill="x", padx=80, pady=20)

        create_button = self.make_button(
            button_frame,
            "Create",
            self.create_reservation,
        )
        create_button.pack(side="left", padx=(0, 8))

        cancel_button = self.make_button(
            button_frame,
            "Cancel",
            lambda: self.load_panel("reservations"),
        )
        cancel_button.pack(side="left")

    def find_customer(self) -> dict:
        """Find customer by id."""
        for customer in self._controller.customers:
            if customer["User ID"] == self.item_id:
                return customer

        return {
            "Name": "",
            "Phone": "",
            "Email": "",
        }

    def get_selected_amenities(self) -> str:
        """Return selected amenities."""
        selected = []
        indexes = self.amenity_listbox.curselection()

        for index in indexes:
            selected.append(
                self.amenity_listbox.get(index)
            )

        return ", ".join(selected)

    def is_valid_dates(self) -> bool:
        """Validate check-in and check-out dates."""
        try:
            checkin = datetime.strptime(
                self.checkin_entry.get(),
                "%m/%d/%Y",
            )

            checkout = datetime.strptime(
                self.checkout_entry.get(),
                "%m/%d/%Y",
            )

            if checkout <= checkin:
                messagebox.showerror(
                    "Error",
                    "Check-out date must be after check-in date.",
                )
                return False

            return True

        except ValueError:
            messagebox.showerror(
                "Error",
                "Dates must use MM/DD/YYYY format.",
            )
            return False

    def is_room_available(self, room_number: str) -> bool:
        """Check if room is available for selected dates."""
        new_checkin = datetime.strptime(
            self.checkin_entry.get(),
            "%m/%d/%Y",
        )

        new_checkout = datetime.strptime(
            self.checkout_entry.get(),
            "%m/%d/%Y",
        )

        for reservation in self._controller.reservations:
            if reservation.get("Room", "") != room_number:
                continue

            if reservation.get("Status", "") in [
                "Cancelled",
                "Checked-out",
            ]:
                continue

            old_checkin = datetime.strptime(
                reservation.get("Date in", ""),
                "%m/%d/%Y",
            )

            old_checkout = datetime.strptime(
                reservation.get("Check-out", ""),
                "%m/%d/%Y",
            )

            dates_overlap = (
                new_checkin < old_checkout
                and new_checkout > old_checkin
            )

            if dates_overlap:
                messagebox.showerror(
                    "Error",
                    "This room is already reserved during those dates.",
                )
                return False

        return True

    def create_reservation(self) -> None:
        """Create reservation."""
        if self.guest_entry.get().strip() == "":
            messagebox.showerror(
                "Error",
                "Guest name is required.",
            )
            return

        if self.room_combo.get().strip() == "":
            messagebox.showerror(
                "Error",
                "Please select a room.",
            )
            return

        if not self.is_valid_dates():
            return

        if not self.is_room_available(self.room_combo.get()):
            return

        new_id = str(
            1000 + len(self._controller.reservations) + 1
        )

        reservation = {
            "Res ID": new_id,
            "Type": "Standard",
            "Date in": self.checkin_entry.get(),
            "Paid": "No",
            "Status": "Reserved",
            "Guest": self.guest_entry.get(),
            "Room": self.room_combo.get(),
            "Amenities": self.get_selected_amenities(),
            "Phone": self.phone_entry.get(),
            "Email": self.email_entry.get(),
            "Check-out": self.checkout_entry.get(),
            "Total": self.total_entry.get(),
        }

        self._controller.reservations.append(
            reservation
        )

        self._controller.save_reservations()

        messagebox.showinfo(
            "Success",
            "Reservation created successfully.",
        )

        self.load_panel("reservations")
