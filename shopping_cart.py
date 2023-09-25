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

def display_total(Total):
    """displays total price after calculations

    Args:
        total (_int): total price
    """
    print("Total price: " + Total)

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)

