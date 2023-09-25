"""
Calculates and displays the total price
of items in a shopping cart.

Functions:
- calculate_total(cart): Calculates the total price of items in the cart.
- display_total(total): Displays the total price.

Example Usage:
CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
"""


def calculate_total(cart):
    """Calculate total price of items in cart.

    Args:
    ----
        cart (list): List of dictionaries containing items and their prices.

    Returns:
    -------
        float: Total price.
    """
    total = 0.0
    for product in cart:
        price = float(product['price'])
        total += price
    return total


def display_total(total):
    """Display total price after calculations.

    Args:
    ----
        total (float): Total price.
    """
    print("Total price: " + str(total))


CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
