
from flask import Flask, render_template, request

app = Flask(__name__)

# Restaurant menu and prices

MENU = {
    # Mysuru and South Indian favourites
    "Mysore Masala Dosa": 80,
    "Idli Vada": 50,
    "Bisi Bele Bath": 70,
    "Pongal": 60,
    "Poori Sagu": 70,
    "Mangalore Bajji": 50,

    # Chaats and snacks
    "Pani Puri": 40,
    "Masala Puri": 50,
    "Bhel Puri": 45,
    "Sev Puri": 50,
    "Samosa": 25,
    "Veg Sandwich": 60,

    # Sweets
    "Mysore Pak": 40,
    "Gulab Jamun": 40,

    # Drinks
    "Filter Coffee": 25,
    "Masala Tea": 20,
    "Badam Milk": 40,
    "Fresh Lime Soda": 35,
    "Mango Juice": 50,
    "Cold Coffee": 60
}

CATEGORIES = {
    "Mysuru Specials": [
        "Mysore Masala Dosa", "Idli Vada", "Bisi Bele Bath",
        "Pongal", "Poori Sagu", "Mangalore Bajji"
    ],
    "Chaats & Snacks": [
        "Pani Puri", "Masala Puri", "Bhel Puri",
        "Sev Puri", "Samosa", "Veg Sandwich"
    ],
    "Sweets & Desserts": [
        "Mysore Pak", "Gulab Jamun"
    ],
    "Drinks & Beverages": [
        "Filter Coffee", "Masala Tea", "Badam Milk",
        "Fresh Lime Soda", "Mango Juice", "Cold Coffee"
    ]
}



@app.route("/")
def home():
    return render_template(
        "index.html",
        menu=MENU,
        categories=CATEGORIES
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/order", methods=["POST"])
def order():
    customer_name = request.form.get("customer_name", "").strip()

    if not customer_name:
        return render_template(
            "result.html",
            error="Please enter your name.",
            order=None
        )

    order_items = []
    total = 0

    for item, price in MENU.items():
        quantity_text = request.form.get(item, "0").strip()

        try:
            quantity = int(quantity_text)
        except ValueError:
            return render_template(
                "result.html",
                error=f"Invalid quantity for {item}. Please enter a whole number.",
                order=None
            )

        if quantity < 0:
            return render_template(
                "result.html",
                error="Quantity cannot be negative.",
                order=None
            )

        if quantity > 100:
            return render_template(
                "result.html",
                error="Quantity cannot exceed 100 for any item.",
                order=None
            )

        if quantity > 0:
            subtotal = price * quantity
            total += subtotal

            order_items.append({
                "name": item,
                "price": price,
                "quantity": quantity,
                "subtotal": subtotal
            })

    if not order_items:
        return render_template(
            "result.html",
            error="Please select at least one food item.",
            order=None
        )

    order = {
        "customer_name": customer_name,
        "items": order_items,
        "total": total
    }

    return render_template(
        "result.html",
        error=None,
        order=order
    )


if __name__ == "__main__":
    app.run(debug=True)
