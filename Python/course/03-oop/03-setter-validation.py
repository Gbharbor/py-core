"""
Lesson: Setter Validation

The product price is validated before being stored.
"""


class Product:
    """Product with price validation using a setter."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        value = float(value)

        if value <= 0:
            raise ValueError("Price must be greater than zero.")

        self._price = value


product = Product("Keyboard", 100)
product.price = 80

print(f"{product.name} - $ {product.price}")