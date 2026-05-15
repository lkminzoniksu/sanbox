# Hotel PieCharm

Hotel PieCharm is a hotel management system developed in Python using both a desktop GUI application and a Flask web application. The project was created for the CC 410 course at Kansas State University and demonstrates object-oriented programming, software engineering principles, testing, validation, and responsive web design.

The application allows users to manage hotel rooms, customers, reservations, invoices, and reports through both desktop and web interfaces.

---

# Features

## Desktop GUI Application

Built with Tkinter.

### Features
- Room management
- Customer management
- Reservation management
- Invoice panel
- Reports dashboard
- Room filtering
- Reservation validation
- Date validation
- Automatic room availability checking

---

## Flask Web Application

Built with Flask and Bootstrap 5.

### Features
- Responsive Bootstrap design
- Mobile hamburger navigation
- Home dashboard
- Room filtering
- Customer CRUD operations
- Reservation CRUD operations
- Reservation search
- Invoice pages
- Reports page
- Automatic room availability filtering
- Date overlap prevention

---

# Cool Feature

One of the main features of the project is the automatic reservation validation system.

The system automatically:
- Prevents overlapping reservations
- Prevents double booking of rooms
- Prevents invalid date ranges
- Filters unavailable rooms based on selected dates
- Updates room availability dynamically

This feature demonstrates functional business logic beyond simply storing data.

---

# Technologies Used

- Python 3
- Tkinter
- Flask
- Flask-Classful
- Flask-WTF
- Bootstrap 5
- JSON Persistence
- Object-Oriented Programming
- pytest
- tox
- mypy
- flake8
- coverage
- pdoc

---

# Object-Oriented Design

The project demonstrates several important object-oriented programming concepts.

## Inheritance

The `Room` abstract class is extended by:
- `StandardRoom`
- `DeluxeRoom`
- `SuiteRoom`
- `PenthouseRoom`

## Interfaces

The `Billable` interface is implemented by room classes to support billing and pricing calculations.

## MVC-Inspired Structure

The project separates:
- Data models
- User interfaces
- Controllers
- Validation logic

---

# Project Structure

```text
src/hotel/
│
├── data/
│   ├── customer/
│   ├── enums/
│   ├── hotel/
│   ├── interfaces/
│   ├── reservation/
│   └── room/
│
├── gui/
│   ├── panels/
│   └── PrimaryWindow.py
│
├── web/
│   ├── forms/
│   └── HotelController.py
│
├── templates/
│
├── Main.py
├── Web.py
└── webapp.py
```

---

# Running the Desktop Application

```bash
python3 -m src
```

---

# Running the Flask Web Application

```bash
python3 -m src web
```

The Flask application will run locally and can be accessed in a browser.

---

# Web Application Features

## Rooms
- View hotel rooms
- Filter by:
  - Room type
  - Smoking
  - Pets
  - Status

## Customers
- Create customers
- Edit customers
- Delete customers
- Search customers

## Reservations
- Create reservations
- Edit reservations
- Delete reservations
- Cancel reservations
- Search reservations
- Generate invoices
- Validate room availability
- Prevent overlapping reservations

## Reports
- Total rooms
- Reserved rooms
- Free rooms
- Occupied rooms
- Total customers
- Total reservations

---

# Reservation Validation

The reservation system prevents:
- Check-out before check-in
- Overlapping reservations
- Double booking of rooms

Rooms automatically become unavailable for overlapping reservation dates.

---

# Testing

The project includes extensive automated unit testing using pytest.

## Tested Components
- Room classes
- Customer class
- Reservation class
- Enums
- Interfaces
- Billing calculations
- Reservation validation logic

## Results
- 183 passing unit tests
- High code coverage
- Successful mypy type checking
- Successful flake8 validation

## Run Tests

```bash
pytest
```

## Run Full Project Validation

```bash
tox
```

---

# UML Diagram

The project includes a complete UML class diagram documenting:
- Classes
- Interfaces
- Enums
- Inheritance
- Relationships
- Multiplicity

---

# Future Improvements

Possible future improvements include:
- Database integration
- User authentication
- Online payment processing
- Admin dashboard
- Cloud deployment
- Reservation analytics

---

# Author

Lucas Minzoni  
Kansas State University  
Bachelor of Science in Integrated Computer Science  

---

# License

Educational project developed for academic purposes.