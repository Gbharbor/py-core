"""
Lista de Compras com Persistência em TXT
"""

ARQUIVO = "shop-list.example"

# garante que o arquivo existe
with open(ARQUIVO, "a"):
    pass


def ler_lista():
    with open(ARQUIVO, "r") as arquivo:
        return [linha.strip() for linha in arquivo]


def exibir_lista(lista):
    print("\n=== LISTA DE COMPRAS ===")

    if not lista:
        print("Lista vazia.")
    else:
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")

    print()


def adicionar_item(item):
    with open(ARQUIVO, "a") as arquivo:
        arquivo.write(item + "\n")


while True:
    lista = ler_lista()
    exibir_lista(lista)

    print("1 - Add. Item")
    print("2 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        novo_item = input("Digite o nome do item: ").strip()

        if novo_item:
            adicionar_item(novo_item)
            print("Item adicionado!\n")
        else:
            print("Item invalido.\n")

    elif opcao == "2":
        print("Saindo...")
        break

    else:
        print("Opcao invalida.\n")
