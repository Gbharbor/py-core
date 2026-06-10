"""
Lesson: Static Method

A static method belongs to the class, but does not depend on object data.
"""


class TextFormatter:
    """Utility class for text formatting."""

    @staticmethod
    def uppercase(value):
        return value.upper()


product_name = TextFormatter.uppercase(
    input("What is the product name? ")
)

print(product_name)