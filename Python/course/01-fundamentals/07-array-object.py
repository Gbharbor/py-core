"""
Lista de Dicionarios (Modelagem de Dados)
"""

print("=== LISTA SIMPLES ===")

nomes = ["gui", "joao"]
print(nomes)


print("\n=== LISTA DE DICIONARIOS ===")

usuarios = [
    {"nome": "gui", "idade": 20},
    {"nome": "ana", "idade": 30},
]

print(usuarios)


print("\n=== APPEND ===")

usuarios.append({"nome": "fulano", "idade": 90})
print(usuarios)


print("\n=== FUNCAO PARA ADICIONAR ===")


def novo_usuario(nome, idade):
    usuarios.append({"nome": nome, "idade": idade})


novo_usuario("Ciclano", 30)
novo_usuario("Guilherme", 340)

print(usuarios)


print("\n=== LOOP ===")

for usuario in usuarios:
    print(f"{usuario['nome']} tem {usuario['idade']} anos.")


print("\n=== FINAL ===")
print(usuarios)
