"""Entry point for the Hotel application."""


from src.hotel.gui.PrimaryWindow import PrimaryWindow


def main() -> None:
    """Run the hotel GUI."""
    window = PrimaryWindow()
    window.mainloop()


if __name__ == "__main__":
    main()
