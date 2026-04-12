"""
Heranca em Programacao Orientada a Objetos
"""


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola, meu nome e {self.nome} e tenho {self.idade} anos.")


class Funcionario(Pessoa):

    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def exibir_salario(self):
        print(f"Meu salario e {self.salario}")


print("=== PESSOA ===")

p1 = Pessoa("Gui", 28)
p1.apresentar()


print("\n=== FUNCIONARIO ===")

f1 = Funcionario("Ana", 20, 3000)

f1.apresentar()
f1.exibir_salario()
