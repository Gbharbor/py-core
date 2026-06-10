"""
Lesson: Class Method

A class method works with class-level data instead of individual object data.
"""


class User:
    """Represents a user and keeps track of all created users."""

    users = []

    def __init__(self, name):
        self.name = name
        User.users.append(self)

    def greet(self):
        print(f"Hello, I am {self.name}")

    @classmethod
    def total_users(cls):
        return len(cls.users)


user_1 = User("Guilherme")
user_2 = User("Pedro")
user_3 = User("Ana")

user_1.greet()

print(f"Total users: {User.total_users()}")