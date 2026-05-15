"""Flask-WTF form for hotel reservations."""

from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    SelectField,
    SelectMultipleField,
    SubmitField,
)
from wtforms.validators import DataRequired


class ReservationForm(FlaskForm):
    """Form for creating hotel reservations."""

    guest = SelectField(
        "Guest",
        choices=[],
        validators=[
            DataRequired(
                message="Guest is required.",
            ),
        ],
    )

    room = SelectField(
        "Room",
        choices=[],
        validators=[
            DataRequired(
                message="Room is required.",
            ),
        ],
    )

    checkin = DateField(
        "Check-in",
        format="%Y-%m-%d",
        validators=[
            DataRequired(
                message="Check-in date is required.",
            ),
        ],
    )

    checkout = DateField(
        "Check-out",
        format="%Y-%m-%d",
        validators=[
            DataRequired(
                message="Check-out date is required.",
            ),
        ],
    )

    amenities = SelectMultipleField(
        "Amenities",
        choices=[],
    )

    status = SelectField(
        "Status",
        choices=[
            ("Reserved", "Reserved"),
            ("Checked-in", "Checked-in"),
            ("Checked-out", "Checked-out"),
            ("Cancelled", "Cancelled"),
        ],
        validators=[
            DataRequired(
                message="Status is required.",
            ),
        ],
    )

    submit = SubmitField("Create Reservation")
