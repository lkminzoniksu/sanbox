"""Reservation view panel."""

import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import ttk

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.gui.ParentPanel import ParentPanel


class ReservationViewPanel(ParentPanel):
    """Panel to view, edit, update, checkout, and cancel reservations."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize reservation view panel."""
        super().__init__(master, controller)

        self.item_id = item_id
        self.reservation = self.find_reservation()

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Reservations / View")

        card = self.make_card(body)

        title = tk.Label(
            card,
            text="View Reservation",
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 20, "bold"),
        )
        title.pack(pady=(30, 20))

        form = tk.Frame(card, bg=self.panel_bg)
        form.pack(fill="x", padx=80, pady=10)

        self.id_entry = self.make_entry_row(
            form,
            "Res ID:",
            self.reservation.get("Res ID", ""),
        )

        self.guest_entry = self.make_entry_row(
            form,
            "Guest:",
            self.reservation.get("Guest", ""),
        )

        self.room_entry = self.make_entry_row(
            form,
            "Room:",
            self.reservation.get("Room", ""),
        )

        self.checkin_entry = self.make_entry_row(
            form,
            "Check-in:",
            self.reservation.get("Date in", ""),
        )

        self.checkout_entry = self.make_entry_row(
            form,
            "Check-out:",
            self.reservation.get("Check-out", ""),
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
            height=5,
            exportselection=False,
            bg="white",
            fg="black",
            selectbackground="#6f35c7",
            selectforeground="white",
            font=("Arial", 12),
            activestyle="none",
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

        self.load_selected_amenities()

        self.total_entry = self.make_entry_row(
            form,
            "Total:",
            self.reservation.get("Total", "$350.00"),
        )

        status_row = tk.Frame(form, bg=self.panel_bg)
        status_row.pack(fill="x", pady=5)

        status_label = tk.Label(
            status_row,
            text="Status:",
            bg=self.panel_bg,
            width=12,
            anchor="w",
        )
        status_label.pack(side="left")

        self.status_combo = ttk.Combobox(
            status_row,
            values=[
                "Reserved",
                "Checked-in",
                "Checked-out",
                "Cancelled",
            ],
            state="readonly",
        )
        self.status_combo.set(
            self.reservation.get("Status", "Reserved")
        )
        self.status_combo.pack(
            side="left",
            fill="x",
            expand=True,
        )

        self.disable_entries()

        button_frame = tk.Frame(card, bg=self.panel_bg)
        button_frame.pack(fill="x", padx=80, pady=20)

        edit_button = self.make_button(
            button_frame,
            "Edit",
            self.enable_edit,
        )
        edit_button.pack(side="left", padx=(0, 8))

        save_button = self.make_button(
            button_frame,
            "Save",
            self.update_reservation,
        )
        save_button.pack(side="left", padx=(0, 8))

        checkout_button = self.make_button(
            button_frame,
            "Check-out",
            self.check_out_reservation,
        )
        checkout_button.pack(side="left", padx=(0, 8))

        cancel_res_button = self.make_button(
            button_frame,
            "Cancel Reservation",
            self.cancel_reservation,
        )
        cancel_res_button.pack(side="left", padx=(0, 8))

        return_button = self.make_button(
            button_frame,
            "Return",
            lambda: self.load_panel("reservations"),
        )
        return_button.pack(side="left")

    def find_reservation(self) -> dict:
        """Find reservation by id."""
        for reservation in self._controller.reservations:
            if reservation.get("Res ID", "") == self.item_id:
                return reservation

        if len(self._controller.reservations) > 0:
            return self._controller.reservations[0]

        return {
            "Res ID": "",
            "Guest": "",
            "Room": "",
            "Date in": "",
            "Check-out": "",
            "Amenities": "",
            "Total": "$350.00",
            "Status": "",
        }

    def disable_entries(self) -> None:
        """Disable entries but keep text readable."""
        entries = [
            self.id_entry,
            self.guest_entry,
            self.room_entry,
            self.checkin_entry,
            self.checkout_entry,
            self.total_entry,
        ]

        for entry in entries:
            entry.config(
                state="readonly",
                readonlybackground="white",
                fg="black",
            )

        self.amenity_listbox.config(
            bg="#f3f3f3",
            fg="black",
        )

        self.amenity_listbox.bind(
            "<<ListboxSelect>>",
            lambda event: "break",
        )

    def enable_edit(self) -> None:
        """Enable reservation editing."""
        self.guest_entry.config(state="normal", fg="black")
        self.checkin_entry.config(state="normal", fg="black")
        self.checkout_entry.config(state="normal", fg="black")
        self.total_entry.config(state="normal", fg="black")
        self.amenity_listbox.config(
            bg="white",
        )

        self.amenity_listbox.unbind(
            "<<ListboxSelect>>"
        )

    def load_selected_amenities(self) -> None:
        """Select saved amenities in listbox."""
        saved = self.reservation.get("Amenities", "")
        saved_list = []

        for item in saved.split(","):
            saved_list.append(item.strip())

        for index in range(self.amenity_listbox.size()):
            value = self.amenity_listbox.get(index)

            if value in saved_list:
                self.amenity_listbox.selection_set(index)

    def get_selected_amenities(self) -> str:
        """Return selected amenities."""
        selected = []
        indexes = self.amenity_listbox.curselection()

        for index in indexes:
            selected.append(
                self.amenity_listbox.get(index)
            )

        return ", ".join(selected)

    def update_reservation(self) -> None:
        """Update reservation information and recalculate total."""
        checkin = self.checkin_entry.get()
        checkout = self.checkout_entry.get()
        room_number = self.room_entry.get()

        nights = self.calculate_nights(
            checkin,
            checkout,
        )

        rate = self.get_room_rate(
            room_number,
        )

        total = nights * rate

        self.reservation["Guest"] = self.guest_entry.get()
        self.reservation["Date in"] = checkin
        self.reservation["Check-out"] = checkout
        self.reservation["Amenities"] = self.get_selected_amenities()
        self.reservation["Total"] = f"${total:.2f}"
        self.reservation["Status"] = self.status_combo.get()

        self.update_room_status()
        self._controller.save_rooms()
        self._controller.save_reservations()

        messagebox.showinfo(
            "Success",
            f"Reservation updated.\nTotal: ${total:.2f}",
        )

        self.load_panel("reservations")

    def update_room_status(self) -> None:
        """Update room status based on reservation status."""
        room_number = self.reservation.get("Room", "")
        status = self.reservation.get("Status", "")

        for room in self._controller.rooms:
            if room["Room"] == room_number:
                if status == "Checked-in":
                    room["Status"] = "Occupied"
                elif status == "Checked-out":
                    room["Status"] = "Free"
                elif status == "Cancelled":
                    room["Status"] = "Free"
                else:
                    room["Status"] = "Reserved"

    def calculate_nights(self, checkin: str, checkout: str) -> int:
        """Calculate number of nights."""
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
        """Get room rate based on room type."""
        for room in self._controller.rooms:
            if room["Room"] == room_number:
                room_type = room.get("Type", "")

                if room_type == "Standart":
                    return 100.00

                if room_type == "Deluxe":
                    return 150.00

                if room_type == "Suite":
                    return 250.00

                if room_type == "Penthouse":
                    return 500.00

        return 100.00

    def check_out_reservation(self) -> None:
        """Check out reservation and generate invoice."""
        checkin = self.reservation.get("Date in", "")
        checkout = self.reservation.get("Check-out", "")
        room_number = self.reservation.get("Room", "")

        nights = self.calculate_nights(checkin, checkout)
        rate = self.get_room_rate(room_number)
        total = nights * rate

        self.reservation["Status"] = "Checked-out"
        self.reservation["Total"] = f"${total:.2f}"
        self.status_combo.set("Checked-out")

        self.update_room_status()
        self._controller.save_rooms()
        self._controller.save_reservations()

        self.load_panel(
            "invoice",
            self.reservation.get("Res ID", ""),
        )

    def cancel_reservation(self) -> None:
        """Remove reservation and free the room."""
        answer = messagebox.askyesno(
            "Cancel Reservation",
            "Are you sure you want to cancel this reservation?",
        )

        if not answer:
            return

        room_number = self.reservation.get("Room", "")

        for room in self._controller.rooms:
            if room["Room"] == room_number:
                room["Status"] = "Free"

        self._controller.save_rooms()

        if self.reservation in self._controller.reservations:
            self._controller.reservations.remove(
                self.reservation
            )

        self._controller.save_reservations()

        messagebox.showinfo(
            "Success",
            "Reservation cancelled.",
        )

        self.load_panel("reservations")
