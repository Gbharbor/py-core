"""
Encapsulamento com Getters e Setters
"""


class Product:

    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_name(self, new_name):
        self._name = new_name

    def set_price(self, new_price):
        self._price = float(new_price)


print("=== INSTANCIAS ===")

p1 = Product("CD", 20)
p2 = Product("DVD", 40)


print("\n=== ACESSO DIRETO ===")

print(p1._name)
p1._name = "Pendrive"
print(p1._name)


print("\n=== GETTERS ===")

print(p1.get_name())


print("\n=== SETTERS ===")

p1.set_name("SSD")
p1.set_price(30)

print(f"O produto {p1.get_name()} custa {p1.get_price()}€")
