"""
Funcoes em Python
"""


def somar(x, y):
    return x + y


print("=== USANDO VALORES FIXOS ===")

resultado = somar(10, 8)
print(f"Total: {resultado}")


print("\n=== USANDO INPUT ===")

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

resultado = somar(numero1, numero2)
print(f"Resultado: {resultado}")
