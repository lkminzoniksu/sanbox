"""Reports panel."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel


class ReportsPanel(ParentPanel):
    """Panel to display hotel reports."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize reports panel."""
        super().__init__(master, controller)

        self.make_header("Hotel PieCharm")

        body = tk.Frame(self, bg=self.background)
        body.pack(fill="both", expand=True)

        self.make_path(body, "/ Reports")

        card = self.make_card(body)

        title = tk.Label(
            card,
            text="Hotel Reports",
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 22, "bold"),
        )
        title.pack(pady=(8, 8))

        total_rooms = len(self._controller.rooms)
        total_customers = len(self._controller.customers)
        total_reservations = len(self._controller.reservations)

        free_rooms = 0
        occupied_rooms = 0
        reserved_rooms = 0
        pet_rooms = 0
        smoker_rooms = 0

        standard_rooms = 0
        deluxe_rooms = 0
        suite_rooms = 0
        penthouse_rooms = 0

        for room in self._controller.rooms:
            status = room.get("Status", "")
            room_type = room.get("Type", "").strip().lower()

            if status == "Free":
                free_rooms += 1

            elif status == "Occupied":
                occupied_rooms += 1

            elif status == "Reserved":
                reserved_rooms += 1

            if room.get("Pet", "No") == "Yes":
                pet_rooms += 1

            if room.get("Smoking", "No") == "Yes":
                smoker_rooms += 1

            if room_type == "standard":
                standard_rooms += 1

            elif room_type == "deluxe":
                deluxe_rooms += 1

            elif room_type == "suite":
                suite_rooms += 1

            elif room_type == "penthouse":
                penthouse_rooms += 1

        report_frame = tk.Frame(card, bg=self.panel_bg)
        report_frame.pack(fill="x", padx=120, pady=2)

        reports = [
            ("Total Rooms", total_rooms),
            ("Free Rooms", free_rooms),
            ("Occupied Rooms", occupied_rooms),
            ("Reserved Rooms", reserved_rooms),
            ("Pet Rooms Available", pet_rooms),
            ("Smoking Rooms Available", smoker_rooms),
            ("Total Customers", total_customers),
            ("Total Reservations", total_reservations),
            ("Standard Rooms ($100)", standard_rooms),
            ("Deluxe Rooms ($150)", deluxe_rooms),
            ("Suite Rooms ($250)", suite_rooms),
            ("Penthouse Rooms ($500)", penthouse_rooms),
        ]

        for label_text, value in reports:
            row = tk.Frame(report_frame, bg=self.panel_bg)
            row.pack(fill="x", pady=1)

            label = tk.Label(
                row,
                text=label_text + ":",
                bg=self.panel_bg,
                fg="black",
                font=("Arial", 11, "bold"),
                width=28,
                anchor="w",
            )
            label.pack(side="left")

            value_label = tk.Label(
                row,
                text=str(value),
                bg="white",
                fg=self.purple,
                font=("Arial", 11),
                relief="solid",
                bd=1,
                padx=10,
                pady=2,
                width=10,
            )
            value_label.pack(side="left")

        bottom_text = tk.Label(
            card,
            text=(
                "Room rates: "
                "Standard $100 | "
                "Deluxe $150 | "
                "Suite $250 | "
                "Penthouse $500"
            ),
            bg=self.panel_bg,
            fg="#666666",
            font=("Arial", 10),
        )
        bottom_text.pack(pady=(10, 6))
