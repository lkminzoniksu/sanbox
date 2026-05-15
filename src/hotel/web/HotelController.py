"""Web controller for Hotel PieCharm pages."""

import json
from datetime import datetime

from flask import redirect, render_template, request
from flask_classful import FlaskView, route

from src.hotel.data.enums.Amenity import Amenity
from src.hotel.web.CustomerForm import CustomerForm
from src.hotel.web.ReservationForm import ReservationForm


class HotelController(FlaskView):
    """Controller for hotel website routes."""

    route_base = "/"

    def load_json(self, filename: str) -> list:
        """Load data from a JSON file."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_json(self, filename: str, data: list) -> None:
        """Save data to a JSON file."""
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @route("/")
    def index(self):
        """Display the home page."""
        return render_template("index.html")

    @route("/about/")
    def about(self):
        """Display the about page."""
        return render_template("about.html")

    @route("/rooms/")
    def rooms(self):
        """Display hotel rooms with filters."""
        rooms = self.load_json("rooms.json")

        room_type = request.args.get("type", "All")
        status = request.args.get("status", "All")
        pet = request.args.get("pet", "All")
        smoking = request.args.get("smoking", "All")

        filtered_rooms = []

        for room in rooms:
            matches = True

            if room_type != "All" and room.get("Type", "") != room_type:
                matches = False

            if status != "All" and room.get("Status", "") != status:
                matches = False

            if pet != "All" and room.get("Pet", "") != pet:
                matches = False

            if smoking != "All" and room.get("Smoking", "") != smoking:
                matches = False

            if matches:
                filtered_rooms.append(room)

        return render_template(
            "rooms.html",
            rooms=filtered_rooms,
            room_type=room_type,
            status=status,
            pet=pet,
            smoking=smoking,
        )

    @route("/customers/")
    def customers(self):
        """Display and search customers."""
        customers = self.load_json(
            "customers.json",
        )

        search = request.args.get(
            "search",
            "",
        ).lower()

        filtered_customers = []

        for customer in customers:

            customer_id = customer.get(
                "User ID",
                "",
            ).lower()

            name = customer.get(
                "Name",
                "",
            ).lower()

            phone = customer.get(
                "Phone",
                "",
            ).lower()

            email = customer.get(
                "Email",
                "",
            ).lower()

            if (
                search in customer_id
                or search in name
                or search in phone
                or search in email
                or search == ""
            ):

                filtered_customers.append(
                    customer,
                )

        return render_template(
            "customers.html",
            customers=filtered_customers,
            search=search,
        )

    @route("/customers/new/", methods=["GET"])
    def new_customer_form(self):
        """Display customer form."""
        form = CustomerForm()
        return render_template("customer_form.html", form=form)

    @route("/customers/", methods=["POST"])
    def create_customer(self):
        """Create a new customer."""
        form = CustomerForm()

        if not form.validate_on_submit():
            return render_template("customer_form.html", form=form)

        customers = self.load_json("customers.json")
        new_id = str(1000 + len(customers) + 1)

        customer = {
            "User ID": new_id,
            "Name": form.name.data,
            "Phone": form.phone.data,
            "Email": form.email.data,
            "Address": form.address.data,
        }

        customers.append(customer)
        self.save_json("customers.json", customers)

        return redirect("/customers/")

    @route("/customers/<customer_id>/")
    def view_customer(self, customer_id: str):
        """Display one customer."""
        customers = self.load_json("customers.json")

        for customer in customers:
            if customer.get("User ID", "") == customer_id:
                return render_template(
                    "customer_view.html",
                    customer=customer,
                )

        return redirect("/customers/")

    @route("/customers/<customer_id>/edit/", methods=["GET"])
    def edit_customer_form(self, customer_id: str):
        """Display form to edit a customer."""
        customers = self.load_json("customers.json")

        for customer in customers:
            if customer.get("User ID", "") == customer_id:
                form = CustomerForm()
                form.name.data = customer.get("Name", "")
                form.phone.data = customer.get("Phone", "")
                form.email.data = customer.get("Email", "")
                form.address.data = customer.get("Address", "")

                return render_template(
                    "customer_form.html",
                    form=form,
                    customer_id=customer_id,
                )

        return redirect("/customers/")

    @route("/customers/<customer_id>/edit/", methods=["POST"])
    def update_customer(self, customer_id: str):
        """Update a customer."""
        form = CustomerForm()

        if not form.validate_on_submit():
            return render_template(
                "customer_form.html",
                form=form,
                customer_id=customer_id,
            )

        customers = self.load_json("customers.json")

        for customer in customers:
            if customer.get("User ID", "") == customer_id:
                customer["Name"] = form.name.data
                customer["Phone"] = form.phone.data
                customer["Email"] = form.email.data
                customer["Address"] = form.address.data

        self.save_json("customers.json", customers)

        return redirect("/customers/")

    @route("/customers/<customer_id>/delete/")
    def delete_customer(self, customer_id: str):
        """Delete a customer."""
        customers = self.load_json("customers.json")
        updated_customers = []

        for customer in customers:
            if customer.get("User ID", "") != customer_id:
                updated_customers.append(customer)

        self.save_json("customers.json", updated_customers)

        return redirect("/customers/")

    @route("/reservations/")
    def reservations(self):
        """Display and search reservations."""
        reservations = self.load_json("reservations.json")
        search = request.args.get("search", "").lower()

        filtered_reservations = []

        for reservation in reservations:
            reservation_id = reservation.get("Res ID", "").lower()
            guest = reservation.get("Guest", "").lower()
            room = reservation.get("Room", "").lower()
            status = reservation.get("Status", "").lower()

            if (
                search in reservation_id
                or search in guest
                or search in room
                or search in status
                or search == ""
            ):
                filtered_reservations.append(reservation)

        return render_template(
            "reservations.html",
            reservations=filtered_reservations,
            search=search,
        )

    @route("/reservations/new/", methods=["GET"])
    def new_reservation_form(self):
        """Display reservation form."""
        form = ReservationForm()
        self.setup_reservation_form(form)

        return render_template(
            "reservation_form.html",
            form=form,
        )

    @route("/reservations/", methods=["POST"])
    def create_reservation(self):
        """Create a new reservation."""
        form = ReservationForm()
        self.setup_reservation_form(form)

        if not form.validate_on_submit():
            return render_template(
                "reservation_form.html",
                form=form,
            )

        if not self.valid_reservation_dates(form):
            return render_template(
                "reservation_form.html",
                form=form,
            )

        if not self.room_is_available(form):
            return render_template(
                "reservation_form.html",
                form=form,
            )

        customers = self.load_json("customers.json")
        reservations = self.load_json("reservations.json")

        guest_name = ""

        for customer in customers:
            if customer.get("User ID", "") == form.guest.data:
                guest_name = customer.get("Name", "")

        new_id = str(1000 + len(reservations) + 1)
        total = self.calculate_total(form)

        reservation = {
            "Res ID": new_id,
            "Guest": guest_name,
            "Room": form.room.data,
            "Date in": form.checkin.data.strftime("%m/%d/%Y"),
            "Check-out": form.checkout.data.strftime("%m/%d/%Y"),
            "Amenities": ", ".join(form.amenities.data),
            "Status": form.status.data,
            "Paid": "No",
            "Total": f"${total:.2f}",
        }

        reservations.append(reservation)
        self.save_json("reservations.json", reservations)

        return redirect("/reservations/")

    @route("/reservations/<res_id>/")
    def view_reservation(self, res_id: str):
        """Display one reservation."""
        reservations = self.load_json("reservations.json")

        for reservation in reservations:
            if reservation.get("Res ID", "") == res_id:
                return render_template(
                    "reservation_view.html",
                    reservation=reservation,
                )

        return redirect("/reservations/")

    @route("/reservations/<res_id>/cancel/")
    def cancel_reservation(self, res_id: str):
        """Cancel a reservation."""
        reservations = self.load_json("reservations.json")

        for reservation in reservations:
            if reservation.get("Res ID", "") == res_id:
                reservation["Status"] = "Cancelled"

        self.save_json("reservations.json", reservations)

        return redirect("/reservations/")

    @route("/reservations/<res_id>/invoice/")
    def invoice(self, res_id: str):
        """Display reservation invoice."""
        reservations = self.load_json("reservations.json")

        for reservation in reservations:
            if reservation.get("Res ID", "") == res_id:
                return render_template(
                    "invoice.html",
                    reservation=reservation,
                )

        return redirect("/reservations/")

    @route("/reservations/<res_id>/edit/", methods=["GET"])
    def edit_reservation_form(self, res_id: str):
        """Display form to edit a reservation."""
        reservations = self.load_json("reservations.json")

        for reservation in reservations:
            if reservation.get("Res ID", "") == res_id:
                form = ReservationForm()
                self.setup_reservation_form(form)

                form.guest.data = self.get_customer_id_from_name(
                    reservation.get("Guest", "")
                )
                form.room.data = reservation.get("Room", "")
                form.checkin.data = datetime.strptime(
                    reservation.get("Date in", ""),
                    "%m/%d/%Y",
                ).date()
                form.checkout.data = datetime.strptime(
                    reservation.get("Check-out", ""),
                    "%m/%d/%Y",
                ).date()

                amenities = reservation.get("Amenities", "")
                if amenities == "":
                    form.amenities.data = []
                else:
                    form.amenities.data = amenities.split(", ")

                form.status.data = reservation.get("Status", "Reserved")

                return render_template(
                    "reservation_form.html",
                    form=form,
                    res_id=res_id,
                )

        return redirect("/reservations/")

    @route("/reservations/<res_id>/edit/", methods=["POST"])
    def update_reservation(self, res_id: str):
        """Update a reservation."""
        form = ReservationForm()
        self.setup_reservation_form(form)

        if not form.validate_on_submit():
            return render_template(
                "reservation_form.html",
                form=form,
                res_id=res_id,
            )

        if not self.valid_reservation_dates(form):
            return render_template(
                "reservation_form.html",
                form=form,
                res_id=res_id,
            )

        if not self.room_is_available(form, res_id):
            return render_template(
                "reservation_form.html",
                form=form,
                res_id=res_id,
            )

        reservations = self.load_json("reservations.json")
        customers = self.load_json("customers.json")

        guest_name = ""

        for customer in customers:
            if customer.get("User ID", "") == form.guest.data:
                guest_name = customer.get("Name", "")

        total = self.calculate_total(form)

        for reservation in reservations:
            if reservation.get("Res ID", "") == res_id:
                reservation["Guest"] = guest_name
                reservation["Room"] = form.room.data
                reservation["Date in"] = form.checkin.data.strftime("%m/%d/%Y")
                reservation["Check-out"] = form.checkout.data.strftime(
                    "%m/%d/%Y"
                )
                reservation["Amenities"] = ", ".join(form.amenities.data)
                reservation["Status"] = form.status.data
                reservation["Total"] = f"${total:.2f}"

        self.save_json("reservations.json", reservations)

        return redirect("/reservations/")

    @route("/reservations/<res_id>/delete/")
    def delete_reservation(self, res_id: str):
        """Delete a reservation."""
        reservations = self.load_json("reservations.json")
        updated_reservations = []

        for reservation in reservations:
            if reservation.get("Res ID", "") != res_id:
                updated_reservations.append(reservation)

        self.save_json("reservations.json", updated_reservations)

        return redirect("/reservations/")

    @route("/reports/")
    def reports(self):
        """Display hotel reports."""
        rooms = self.load_json("rooms.json")
        customers = self.load_json("customers.json")
        reservations = self.load_json("reservations.json")

        total_rooms = len(rooms)
        total_customers = len(customers)
        total_reservations = len(reservations)

        free_rooms = 0
        reserved_rooms = 0
        occupied_rooms = 0
        pet_rooms = 0
        smoking_rooms = 0

        for room in rooms:
            if room.get("Status", "") == "Free":
                free_rooms += 1

            elif room.get("Status", "") == "Reserved":
                reserved_rooms += 1

            elif room.get("Status", "") == "Occupied":
                occupied_rooms += 1

            if room.get("Pet", "") == "Yes":
                pet_rooms += 1

            if room.get("Smoking", "") == "Yes":
                smoking_rooms += 1

        return render_template(
            "reports.html",
            total_rooms=total_rooms,
            total_customers=total_customers,
            total_reservations=total_reservations,
            free_rooms=free_rooms,
            reserved_rooms=reserved_rooms,
            occupied_rooms=occupied_rooms,
            pet_rooms=pet_rooms,
            smoking_rooms=smoking_rooms,
        )

    def setup_reservation_form(self, form: ReservationForm) -> None:
        """Add dynamic choices to the reservation form."""
        customers = self.load_json("customers.json")

        if form.checkin.data and form.checkout.data:
            rooms = self.available_rooms(
                form.checkin.data,
                form.checkout.data,
            )
        else:
            rooms = self.load_json("rooms.json")

        form.guest.choices = []

        for customer in customers:
            form.guest.choices.append(
                (
                    customer.get("User ID", ""),
                    customer.get("Name", ""),
                )
            )

        form.room.choices = []

        for room in rooms:
            label = (
                f"{room.get('Room', '')} - "
                f"{room.get('Type', '')} - "
                f"{room.get('Bed', '')}"
            )

            form.room.choices.append(
                (
                    room.get("Room", ""),
                    label,
                )
            )

        form.amenities.choices = []

        for amenity in Amenity:
            form.amenities.choices.append(
                (
                    amenity.value,
                    amenity.value,
                )
            )

    def get_customer_id_from_name(self, customer_name: str) -> str:
        """Return customer id matching a customer name."""
        customers = self.load_json("customers.json")

        for customer in customers:
            if customer.get("Name", "") == customer_name:
                return customer.get("User ID", "")

        return ""

    def valid_reservation_dates(
        self,
        form: ReservationForm,
    ) -> bool:
        """Return whether checkout is after check-in."""
        if form.checkout.data <= form.checkin.data:
            form.checkout.errors.append(
                "Check-out must be after check-in."
            )

            return False

        return True

    def room_is_available(
        self,
        form: ReservationForm,
        current_res_id: str = "",
    ) -> bool:
        """Return whether the selected room is available."""
        reservations = self.load_json("reservations.json")

        new_checkin = form.checkin.data
        new_checkout = form.checkout.data

        for reservation in reservations:
            if reservation.get("Res ID", "") == current_res_id:
                continue

            if reservation.get("Room", "") != form.room.data:
                continue

            if reservation.get("Status", "") in [
                "Cancelled",
                "Checked-out",
            ]:
                continue

            old_checkin = datetime.strptime(
                reservation.get("Date in", ""),
                "%m/%d/%Y",
            ).date()

            old_checkout = datetime.strptime(
                reservation.get("Check-out", ""),
                "%m/%d/%Y",
            ).date()

            overlap = (
                new_checkin < old_checkout
                and new_checkout > old_checkin
            )

            if overlap:
                form.room.errors.append(
                    "This room is already reserved for those dates."
                )

                return False

        return True

    def get_room_rate(self, room_number: str) -> float:
        """Return the nightly rate for a room."""
        rooms = self.load_json("rooms.json")

        for room in rooms:
            if room.get("Room", "") == room_number:
                room_type = room.get("Type", "")

                if room_type == "Standard":
                    return 200.0

                if room_type == "Deluxe":
                    return 300.0

                if room_type == "Suite":
                    return 400.0

                if room_type == "Penthouse":
                    return 500.0

        return 0.0

    def calculate_total(self, form: ReservationForm) -> float:
        """Calculate reservation total."""
        nights = (form.checkout.data - form.checkin.data).days
        rate = self.get_room_rate(form.room.data)

        return nights * rate

    def available_rooms(
        self,
        checkin,
        checkout,
    ) -> list:
        """Return available rooms for the selected dates."""
        rooms = self.load_json("rooms.json")
        reservations = self.load_json("reservations.json")

        available = []

        for room in rooms:
            room_number = room.get("Room", "")
            room_available = True

            for reservation in reservations:
                if reservation.get("Room", "") != room_number:
                    continue

                if reservation.get("Status", "") in [
                    "Cancelled",
                    "Checked-out",
                ]:
                    continue

                old_checkin = datetime.strptime(
                    reservation.get("Date in", ""),
                    "%m/%d/%Y",
                ).date()

                old_checkout = datetime.strptime(
                    reservation.get("Check-out", ""),
                    "%m/%d/%Y",
                ).date()

                overlap = checkin < old_checkout and checkout > old_checkin

                if overlap:
                    room_available = False
                    break

            if room_available:
                available.append(room)

        return available
