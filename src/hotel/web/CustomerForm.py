"""Flask-WTF form for hotel customers."""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
)


class CustomerForm(FlaskForm):
    """Form for creating and editing customers."""

    name = StringField(
        "Name",
        validators=[
            DataRequired(
                message="Name is required."
            ),
            Length(
                min=2,
                message=(
                    "Name must have at least "
                    "2 characters."
                ),
            ),
        ],
    )

    phone = StringField(
        "Phone",
        validators=[
            DataRequired(
                message="Phone is required."
            ),
            Length(
                min=7,
                message=(
                    "Phone must have at least "
                    "7 characters."
                ),
            ),
        ],
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(
                message="Email is required."
            ),
            Email(
                message="Invalid email address."
            ),
        ],
    )

    address = StringField(
        "Address",
        validators=[
            DataRequired(
                message="Address is required."
            ),
            Length(
                min=3,
                message=(
                    "Address must have at least "
                    "3 characters."
                ),
            ),
        ],
    )

    submit = SubmitField("Save Customer")
