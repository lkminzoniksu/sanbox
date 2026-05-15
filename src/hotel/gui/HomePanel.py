"""Home panel for hotel GUI."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel


class HomePanel(ParentPanel):
    """Main menu panel for the hotel GUI."""

    def __init__(self, master, controller, item_id: str = "") -> None:
        """Initialize the home panel."""
        super().__init__(master, controller)

        sidebar = tk.Frame(self, bg="#eee5f8", width=230)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        name = tk.Label(
            sidebar,
            text="Hotel PieCharm",
            bg="#eee5f8",
            fg="#3b176b",
            font=("Arial", 13, "bold"),
        )
        name.pack(pady=(80, 25))

        buttons = [
            ("Rooms", "rooms"),
            ("Book Room", "reservation_create"),
            ("Customers", "customers"),
            ("Reservations", "reservations"),
            ("Reports", "reports"),
        ]

        for text, panel in buttons:
            button = self.make_button(
                sidebar,
                text,
                lambda p=panel: self.load_panel(p),
                width=22,
            )
            button.pack(fill="x", padx=18, pady=7)

        main = tk.Frame(self, bg=self.background)
        main.pack(side="left", fill="both", expand=True)
        title = tk.Label(
            main,
            text="Welcome to Hotel PieCharm",
            bg=self.background,
            fg="#1d102e",
            font=("Arial", 22, "bold"),
            anchor="w",
        )
        title.pack(fill="x", padx=35, pady=(35, 6))

        subtitle = tk.Label(
            main,
            text="Manage rooms, customers, and reservations.",
            bg=self.background,
            fg="#3b176b",
            font=("Arial", 12),
            anchor="w",
        )
        subtitle.pack(fill="x", padx=35)

        card = tk.Frame(
            main,
            bg="white",
            highlightbackground="#d9c8e9",
            highlightthickness=1,
        )
        card.pack(fill="both", expand=True, padx=35, pady=25)

        big_icon = tk.Label(
            card,
            text="Hotel PieCharm",
            bg="white",
            fg=self.purple,
            font=("Arial", 30, "bold"),
        )
        big_icon.pack(pady=(70, 10))

        info = tk.Label(
            card,
            text='''Use the purple menu on the left to view rooms,\n
customers, and reservations.\n
Created by Lucas Minzoni\n
CC410 KSU''',
            bg="white",
            fg="#333333",
            font=("Arial", 13),
        )
        info.pack()
