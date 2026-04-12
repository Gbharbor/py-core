"""
Cadastro de Clientes com Encapsulamento
"""


class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_idade(self, nova_idade):
        self._idade = nova_idade


class Cliente(Pessoa):

    def __init__(self, nome, idade, email, ltv):
        super().__init__(nome, idade)
        self._email = email
        self._ltv = float(ltv)

    def get_email(self):
        return self._email

    def get_ltv(self):
        return self._ltv

    def set_email(self, novo_email):
        self._email = novo_email

    def set_ltv(self, novo_ltv):
        self._ltv = float(novo_ltv)


clientes = [
    Cliente("Ana", 20, "ana@gmail.com", 3000),
    Cliente("Gui", 30, "gui@gmail.com", 2230),
]

print("=== CLIENTES CADASTRADOS ===")

soma_ltv = 0

for cliente in clientes:
    print(
        f"Nome: {cliente.get_nome()} | "
        f"Idade: {cliente.get_idade()} | "
        f"Email: {cliente.get_email()} | "
        f"LTV: ${cliente.get_ltv()}"
    )
    soma_ltv += cliente.get_ltv()

print("\n=== TOTAL LTV ===")
print(f"${soma_ltv}")
