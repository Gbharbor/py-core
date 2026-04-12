"""
Lista de Compras com Persistência em TXT (OOP)
"""


class ListaCompras:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.garantir_arquivo()

    def garantir_arquivo(self):
        with open(self.arquivo, "a"):
            pass

    def ler_lista(self):
        with open(self.arquivo, "r") as arquivo:
            return [linha.strip() for linha in arquivo]

    def exibir_lista(self):
        lista = self.ler_lista()

        print("\n=== LISTA DE COMPRAS ===")

        if not lista:
            print("Lista vazia.")
        else:
            for i, item in enumerate(lista, start=1):
                print(f"{i}. {item}")

        print()

    def adicionar_item(self, item):
        with open(self.arquivo, "a") as arquivo:
            arquivo.write(item + "\n")

    def item_existe(self, item):
        return any(
            item_lista.lower() == item.lower() for item_lista in self.ler_lista()
        )

    def comparar_listas(self, outra_lista):
        lista_atual = self.ler_lista()
        return [item for item in lista_atual if item in outra_lista]


lista_compras = ListaCompras("shop-list.example")

while True:
    lista_compras.exibir_lista()

    print("1 - Adicionar item")
    print("2 - Verificar se item existe")
    print("3 - Comparar com outra lista")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        novo_item = input("Digite o nome do item: ").strip()

        if not novo_item:
            print("Item invalido.\n")
        elif lista_compras.item_existe(novo_item):
            print("Esse item ja existe na lista.\n")
        else:
            lista_compras.adicionar_item(novo_item)
            print("Item adicionado com sucesso!\n")

    elif opcao == "2":
        item = input("Digite o item para verificar: ").strip()

        if lista_compras.item_existe(item):
            print("O item ja esta na lista.\n")
        else:
            print("O item nao esta na lista.\n")

    elif opcao == "3":
        outra_lista = ["arroz", "feijao", "leite", "cafe"]
        itens_em_comum = lista_compras.comparar_listas(outra_lista)

        print(f"Outra lista usada na comparacao: {outra_lista}")

        if itens_em_comum:
            print("Itens em comum:", itens_em_comum, "\n")
        else:
            print("Nao ha itens em comum.\n")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opcao invalida.\n")
