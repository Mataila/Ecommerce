def add_product(product_name: str, price: float, quantity: int) -> dict:
    """Creates and returns a dictionary for the product."""
    return {
        "name": product_name,
        "price": price,
        "quantity": quantity
    }

def update_price(product: dict, new_price: float) -> dict:
    """Updates the price of the given product and returns the modified dictionary."""
    product["price"] = new_price
    return product

def update_quantity(product: dict, quantity_change: int) -> dict:
    """Updates the quantity of the given product and returns the modified dictionary."""
    product["quantity"] += quantity_change
    return product

# Example usage
product = add_product("Laptop", 999.99, 10)
print("Initial Product:", product)

product = update_price(product, 1099.99)
print("After Price Update:", product)

product = update_quantity(product, -2)
print("After Quantity Update:", product)
