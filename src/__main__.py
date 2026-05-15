"""Main entry point for Hotel PieCharm."""

import sys

from src.hotel.Web import Web
from src.hotel.gui.PrimaryWindow import PrimaryWindow


def main() -> None:
    """Run the selected application mode."""

    if len(sys.argv) > 1 and sys.argv[1] == "web":
        app = Web.main(sys.argv)

        app.run(
            host="0.0.0.0",
            port=5000,
            debug=True,
        )

    else:
        window = PrimaryWindow()
        window.mainloop()


if __name__ == "__main__":
    main()
