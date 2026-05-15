"""Flask application for Hotel PieCharm."""

from flask import Flask

from src.hotel.web.HotelController import HotelController


class Web:
    """Configure and create the Flask application."""

    @staticmethod
    def main(args: list[str]) -> Flask:
        """Create and configure the Flask app."""
        app = Flask(__name__)
        app.config["SECRET_KEY"] = "hotelpiecharm"

        HotelController.register(app)

        return app
