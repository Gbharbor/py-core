"""
Lesson: Classes and Objects

Basic example of a class, object creation, attributes and methods.
"""


class Person:
    """Represents a person with a name."""

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}")


person_1 = Person("Bonieky")
person_2 = Person("Pedro")

person_2.greet()