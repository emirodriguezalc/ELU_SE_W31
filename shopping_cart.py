"""
This module calculates and displays the total price 
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
    """calculates total price of items in cart

    Args:
        cart (array):array of items

    Returns: 
        int: total price
    """
    total = 0
    for product in cart:
        total += product['price']
    return total


def display_total(total):
    """displays total price after calculations

    Args:
        total (_int): total price
    """
    print("Total price: " + total)


CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
