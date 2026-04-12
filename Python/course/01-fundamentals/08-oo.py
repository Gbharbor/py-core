"""
Introducao a Classes em Python
"""

print("=== SEM CLASSES ===")


def apresentar(nome, idade):
    print(f"Ola, eu sou {nome} e tenho {idade} anos.")


apresentar("Carlos", 18)


print("\n=== CLASSE ===")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def resumir(self):
        print(f"{self.name} custa {self.price}")


print("\n=== INSTANCIAS ===")

p1 = Product("CD", 20)
p2 = Product("DVD", 40)

p1.resumir()
p2.resumir()
