"""
Listas, Tuplas e Dicionarios
"""

print("=== LISTAS ===")

lista = ["arroz", "feijao", "carne"]
nomes = ["ana", "ju", "gui"]
misto = ["arroz", 1, "gui", "bla"]

print(lista)
print(nomes)
print(misto)

print("\nAcesso por indice:")
print(nomes[0])
print(lista[1])

lista[1] = "lentilha"
print("\nLista atualizada:", lista)


print("\n=== TUPLAS ===")

tupla = ("arroz", "feijao", "carne")

print(tupla)
print("Primeiro elemento:", tupla[0])


print("\n=== DICIONARIOS ===")

pessoa = {"nome": "gui", "idade": 90, "pais": "Brasil"}

print(pessoa)

print("\nAcesso por chave:")
print(pessoa["nome"])
print(pessoa["idade"])

pessoa["idade"] = 100
print("\nIdade atualizada:", pessoa["idade"])

pessoa["profissao"] = "Engenharia"
print("\nDicionario atualizado:", pessoa)


print("\n=== RESUMO ===")
print("Lista -> [] | mutavel | indice")
print("Tupla -> () | imutavel | indice")
print("Dicionario -> {} | mutavel | chave")
