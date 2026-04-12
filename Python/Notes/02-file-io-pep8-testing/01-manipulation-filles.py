"""
Manipulação de Arquivos em Python
"""

ARQUIVO = "arquivo-exemplo.txt"


print("=== WRITE ===")

with open(ARQUIVO, "w") as arquivo:
    arquivo.write("Linha 1: Olá, mundo!\n")
    arquivo.write("Linha 2: Aprendendo Python\n")
    arquivo.writelines(["Gui\n", "Ana\n", "Mari\n"])

print("Arquivo escrito.\n")
print("=== READ ===")

with open(ARQUIVO, "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print()
print("=== APPEND ===")

with open(ARQUIVO, "a") as arquivo:
    arquivo.write("Linha adicionada 1\n")
    arquivo.write("Linha adicionada 2\n")

print("Conteúdo adicionado.\n")
print("=== WITH OPEN ===")

with open(ARQUIVO, "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print()

with open(ARQUIVO, "w") as arquivo:
    arquivo.write("Arquivo sobrescrito\n")
    arquivo.write("Novo conteúdo\n")

print("Arquivo reescrito.")
