"""Parent panel for hotel GUI."""

import tkinter as tk


class ParentPanel(tk.Frame):
    """Base class for all hotel GUI panels."""

    def __init__(self, master, controller) -> None:
        """Initialize the parent panel."""
        super().__init__(master)
        self._controller = controller

    def load_panel(self, panel_name: str) -> None:
        """Ask controller to load another panel."""
        self._controller.load_panel(panel_name)
