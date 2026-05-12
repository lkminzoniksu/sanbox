"""Home panel for hotel GUI."""

import tkinter as tk

from src.hotel.gui.ParentPanel import ParentPanel


class HomePanel(ParentPanel):
    """Main menu panel for the hotel GUI."""

    def __init__(self, master, controller) -> None:
        """Initialize the home panel."""
        super().__init__(master, controller)

        self.configure(bg="#d9d9d9")

        sidebar = tk.Frame(self, bg="#c084dc", width=120)
        sidebar.pack(side="left", fill="y", padx=5, pady=5)
        sidebar.pack_propagate(False)

        main_area = tk.Frame(self, bg="#d9d9d9")
        main_area.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        title = tk.Label(
            main_area,
            text="Hotel PieCharm",
            font=("Arial", 16),
            bg="#c77bea"
        )
        title.pack(fill="x", pady=5)

        spacer = tk.Label(sidebar, text="", bg="#c084dc")
        spacer.pack(pady=45)

        rooms_button = tk.Button(
            sidebar,
            text="Rooms",
            width=12,
            bg="#b347d9",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.load_panel("rooms")
        )
        rooms_button.pack(padx=5, pady=5, fill="x")

        book_button = tk.Button(
            sidebar,
            text="Book Room",
            width=12,
            bg="#b347d9",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.load_panel("book")
        )
        book_button.pack(padx=5, pady=5)

        customers_button = tk.Button(
            sidebar,
            text="Customers",
            width=12,
            bg="#b347d9",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.load_panel("customers")
        )
        customers_button.pack(padx=5, pady=5)

        reservations_button = tk.Button(
            sidebar,
            text="Reservations",
            width=12,
            bg="#b347d9",
            relief="flat",
            bd=0,
            highlightthickness=0,
            command=lambda: self.load_panel("reservations")
        )
        reservations_button.pack(padx=5, pady=5)

        bottom_bar = tk.Label(
            self,
            text="",
            bg="#c77bea"
        )
        bottom_bar.pack(side="bottom", fill="x", padx=5, pady=5)
