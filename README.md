# Mysore Spice Restaurant Menu and Order Calculator

## Project Description
Mysore Spice is a simple restaurant web application developed using Python Flask. Customers can view a vegetarian menu featuring Mysuru specialities, chaats, snacks, sweets, and drinks. They can enter their name, select quantities, and calculate their total bill.

## Technologies Used
- Python
- Flask
- HTML
- CSS

## Project Structure
- app.py — Flask application and order calculation
- templates/index.html — Restaurant menu and order form
- templates/about.html — Restaurant information
- templates/result.html — Order summary and error messages
- static/style.css — Website styling
- requirements.txt — Required Python package

## How to Run the Project
1. Open the project folder in VS Code.
2. Activate the virtual environment in the terminal.
3. Install Flask using: `python -m pip install -r requirements.txt`
4. Run the application using: `python app.py`
5. Open `http://127.0.0.1:5000/` in your browser.

## Application Routes
- GET / — Displays the restaurant menu.
- GET /about — Displays information about the restaurant.
- POST /order — Accepts the order form, validates input, and calculates the bill.

## Input Validation
The application checks for a missing customer name, invalid quantities, negative quantities, quantities above 100, and orders without selected food items.

## Testing
Test the homepage, About page, successful orders, empty orders, and invalid inputs.
