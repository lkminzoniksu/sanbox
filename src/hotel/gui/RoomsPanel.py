"""Rooms panel."""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from src.hotel.gui.ParentPanel import ParentPanel


class RoomsPanel(ParentPanel):
    """Panel to display and filter hotel rooms."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize rooms panel."""
        super().__init__(master, controller)

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Rooms")

        filter_frame = tk.Frame(body, bg=self.background)
        filter_frame.pack(fill="x", padx=18, pady=(5, 5))

        free_button = self.make_button(
            filter_frame,
            "Free Only",
            self.filter_free_rooms,
        )
        free_button.pack(side="left", padx=(0, 8))

        smoking_button = self.make_button(
            filter_frame,
            "Smoking",
            self.filter_smoking_rooms,
        )
        smoking_button.pack(side="left", padx=(0, 8))

        pet_button = self.make_button(
            filter_frame,
            "Pet Friendly",
            self.filter_pet_rooms,
        )
        pet_button.pack(side="left", padx=(0, 8))

        type_label = tk.Label(
            filter_frame,
            text="Type:",
            bg=self.background,
            fg="black",
        )
        type_label.pack(side="left", padx=(10, 5))

        self.type_combo = ttk.Combobox(
            filter_frame,
            values=[
                "All",
                "Standard",
                "Deluxe",
                "Suite",
                "Penthouse",
            ],
            state="readonly",
            width=14,
        )
        self.type_combo.set("All")
        self.type_combo.pack(side="left", padx=(0, 8))

        type_button = self.make_button(
            filter_frame,
            "Apply Type",
            self.filter_by_type,
        )
        type_button.pack(side="left", padx=(0, 8))

        clear_button = self.make_button(
            filter_frame,
            "Clear",
            self.clear_filter,
        )
        clear_button.pack(side="left")

        card = self.make_card(body)

        columns = (
            "Room",
            "Type",
            "Bed",
            "Smoking",
            "Pets",
            "Status",
        )

        self.table = self.make_table(card, columns)

        self.load_rooms(self._controller.rooms)

        button_frame = tk.Frame(body, bg=self.background)
        button_frame.pack(fill="x", padx=18, pady=(0, 16))

        checkin = self.make_button(
            button_frame,
            "Check-in",
            self.check_in,
        )
        checkin.pack(side="left", padx=(0, 8))

        checkout = self.make_button(
            button_frame,
            "Check-out",
            self.check_out,
        )
        checkout.pack(side="left")

    def load_rooms(self, rooms) -> None:
        """Load rooms into the table."""
        for item in self.table.get_children():
            self.table.delete(item)

        for room in rooms:
            values = (
                room.get("Room", ""),
                room.get("Type", ""),
                room.get("Bed", ""),
                room.get("Smoking", ""),
                room.get("Pet", "No"),
                room.get("Status", ""),
            )

            self.table.insert("", "end", values=values)

    def filter_free_rooms(self) -> None:
        """Show only free rooms."""
        results = []

        for room in self._controller.rooms:
            if room.get("Status", "") == "Free":
                results.append(room)

        self.load_rooms(results)

    def filter_smoking_rooms(self) -> None:
        """Show only smoking rooms."""
        results = []

        for room in self._controller.rooms:
            if room.get("Smoking", "No") == "Yes":
                results.append(room)

        self.load_rooms(results)

    def filter_pet_rooms(self) -> None:
        """Show only pet-friendly rooms."""
        results = []

        for room in self._controller.rooms:
            if room.get("Pet", "No") == "Yes":
                results.append(room)

        self.load_rooms(results)

    def filter_by_type(self) -> None:
        """Show rooms by selected type."""
        selected_type = self.type_combo.get()

        if selected_type == "All":
            self.load_rooms(self._controller.rooms)
            return

        results = []

        for room in self._controller.rooms:
            if room.get("Type", "") == selected_type:
                results.append(room)

        self.load_rooms(results)

    def clear_filter(self) -> None:
        """Clear all filters."""
        self.type_combo.set("All")
        self.load_rooms(self._controller.rooms)

    def get_selected_room(self):
        """Get selected room."""
        selected = self.table.selection()

        if len(selected) == 0:
            return None

        values = self.table.item(selected[0], "values")
        room_number = values[0]

        for room in self._controller.rooms:
            if room.get("Room", "") == room_number:
                return room

        return None

    def check_in(self) -> None:
        """Check in a room."""
        room = self.get_selected_room()

        if room is None:
            messagebox.showerror(
                "Error",
                "Please select a room.",
            )
            return

        if room.get("Status", "") == "Occupied":
            messagebox.showerror(
                "Error",
                "Room is already occupied.",
            )
            return

        room["Status"] = "Occupied"
        self._controller.save_rooms()

        self.load_rooms(self._controller.rooms)

        messagebox.showinfo(
            "Success",
            f'Room {room["Room"]} checked in.',
        )

    def check_out(self) -> None:
        """Check out a room."""
        room = self.get_selected_room()

        if room is None:
            messagebox.showerror(
                "Error",
                "Please select a room.",
            )
            return

        if room.get("Status", "") == "Free":
            messagebox.showerror(
                "Error",
                "Room is already free.",
            )
            return

        room["Status"] = "Free"
        self._controller.save_rooms()

        self.load_rooms(self._controller.rooms)

        messagebox.showinfo(
            "Success",
            f'Room {room["Room"]} checked out.',
        )
