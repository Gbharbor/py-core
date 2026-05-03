"""
Aula: Fundamentos de OOP em Python

- Classes e objetos
- Métodos e construtor (__init__)
- Encapsulamento
- @property e @setter
"""

class Pessoa:
    """Representa uma pessoa com nome e ação de saudação."""

    def __init__(self, nome):
        self.nome = nome

    def saudar(self):
        print(f"Olá, eu sou {self.nome}")


p1 = Pessoa("Bonieky")
p2 = Pessoa("Pedro")
p2.saudar()


class Conta:
    """Conta bancária com saldo protegido e operações básicas."""

    def __init__(self):
        self._saldo = 0  # atributo protegido

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += float(valor)

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False


c1 = Conta()
c1.depositar(200)

qt = float(input("Quanto você quer sacar? "))

if c1.sacar(qt):
    print("Saque realizado")
else:
    print("Saldo insuficiente")

print(f"Saldo atual: {c1.saldo}")


class Produto:
    """Produto com validação de preço usando setter."""

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco  # passa pelo setter

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = float(valor)


p1 = Produto("Mouse XYZ", 100)
p1.preco = 10

print(f"{p1.nome} - $ {p1.preco}")