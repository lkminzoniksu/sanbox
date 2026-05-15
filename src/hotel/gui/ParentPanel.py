"""Parent panel for hotel GUI."""

import tkinter as tk
from tkinter import ttk


class ParentPanel(tk.Frame):
    """Base class for all hotel GUI panels."""

    purple = "#6f35b5"
    purple_light = "#c084e8"
    purple_mid = "#a64bd8"
    background = "#f7f3fb"
    panel_bg = "#ffffff"

    def __init__(self, master, controller) -> None:
        """Initialize the parent panel."""
        super().__init__(master, bg=self.background)
        self._controller = controller

    def load_panel(self, panel_name: str, item_id: str = "") -> None:
        """Ask controller to load another panel."""
        self._controller.load_panel(panel_name, item_id)

    def make_button(self, master, text: str, command=None, width: int = 14):
        """Create a purple button."""
        return tk.Button(
            master,
            text=text,
            command=command,
            width=width,
            bg=self.purple,
            fg="white",
            activebackground=self.purple_mid,
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=8,
            pady=5,
            font=("Arial", 10),
        )

    def make_header(self, title: str):
        """Create the header with return button and title."""
        header = tk.Frame(self, bg=self.panel_bg, height=58)
        header.pack(fill="x")
        header.pack_propagate(False)

        return_button = tk.Button(
            header,
            text="← Return",
            command=lambda: self.load_panel("home"),
            bg="#efe6f8",
            fg="#3b176b",
            activebackground="#e2d0f2",
            relief="flat",
            bd=1,
            padx=18,
            pady=6,
        )
        return_button.pack(side="left", padx=16, pady=12)

        title_label = tk.Label(
            header,
            text=title,
            bg=self.panel_bg,
            fg=self.purple,
            font=("Arial", 16, "bold"),
        )
        title_label.pack(side="left", expand=True)

        spacer = tk.Label(header, text="", bg=self.panel_bg, width=12)
        spacer.pack(side="right")

    def make_path(self, master, text: str):
        """Create a path label."""
        path = tk.Label(
            master,
            text=text,
            bg=self.background,
            fg=self.purple,
            anchor="w",
            font=("Arial", 10),
        )
        path.pack(fill="x", padx=18, pady=(12, 4))

    def make_card(self, master):
        """Create a white card frame."""
        card = tk.Frame(
            master,
            bg=self.panel_bg,
            highlightbackground="#d9c8e9",
            highlightthickness=1,
        )
        card.pack(fill="both", expand=True, padx=18, pady=8)
        return card

    def make_entry_row(self, master, label_text: str, value: str = ""):
        """Create a label and entry row."""
        row = tk.Frame(master, bg=self.panel_bg)
        row.pack(fill="x", pady=5)

        label = tk.Label(
            row,
            text=label_text,
            bg=self.panel_bg,
            width=12,
            anchor="w",
        )
        label.pack(side="left")

        entry = tk.Entry(row, relief="solid", bd=1)
        entry.insert(0, value)
        entry.pack(side="left", fill="x", expand=True)

        return entry

    def make_table(self, master, columns):
        """Create a treeview table."""
        style = ttk.Style()
        style.configure("Hotel.Treeview", rowheight=28, font=("Arial", 10))
        style.configure(
            "Hotel.Treeview.Heading",
            font=("Arial", 10, "bold"),
            background=self.purple,
            foreground="white",
        )

        tree = ttk.Treeview(
            master,
            columns=columns,
            show="headings",
            style="Hotel.Treeview",
            height=8,
        )

        for column in columns:
            tree.heading(column, text=column)
            tree.column(column, anchor="center", width=120)

        tree.pack(fill="both", expand=True, padx=8, pady=8)
        return tree
