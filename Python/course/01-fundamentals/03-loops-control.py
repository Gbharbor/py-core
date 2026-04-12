"""
AULA: Loops (while, for) e listas
"""

# while

print("while:")

contador = 1

while contador < 10:
    print(contador)
    contador += 1


# for com range

print("\nfor range(5):")

for numero in range(5):
    print("Executou")
    print(numero)


print("\nfor inicio e fim:")

for numero in range(5, 10):
    print(numero)


print("\nfor com passo:")

for numero in range(0, 10, 2):
    print(numero)


# comparação

print("\n1 a 5 com while:")

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


print("\n1 a 5 com for:")

for numero in range(1, 6):
    print(numero)


# exemplo prático

print("\nexemplo:")

for post in range(10):
    print(f"Exibindo post numero {post + 1}")


# listas

print("\nlista de nomes:")

nomes = ["joao", "ana", "Gui", "Ju"]

for nome in nomes:
    print(f"Nome inscrito: {nome.title()}")

print("- Obrigado pela inscricao!")


# tabuada

print("\ntabuada:")

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in tabuada:
    print(f"{numero} x 2 = {numero * 2}")


# string

print("\nloop em string:")

for letra in "Python":
    print(letra)
