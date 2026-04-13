"""
Introducao a Classes em Python
"""

print("no classes")


def greetings(name, age):
    print(f"hi i am {name} and i have {age} anos.")


greetings("Gui", 95)


print("\n classes")


class Address:
    def __init__(self, mail, city):
        self.mail = mail
        self.city = city

    def summary(self):
        print(f"Postal mail: {self.mail}, city: {self.city} ")


print("\n=== Instance ===")
p1 = Address(2500 - 123, "Lisbon")
p2 = Address(2500 - 321, "Porto")
p1.summary()


p2.summary()
