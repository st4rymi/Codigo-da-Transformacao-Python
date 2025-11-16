print("----------_----------_------")
print(" seja bem vindo ao CDT")
print("----------_----------_------")


Lista_de_compras = [ ]

while True:
    print("\n--- Menu de Compras---")
    print("1. adicionar item")
    print("2. visualizar lista")
    print("3. remover item da lista")
    print("4. sair da lista")

    escolha = input("digite sua escolha: ")

    if escolha == '4' :
        print("Saindo do programa. Até logo!")
        break

    elif escolha == '1':
        item = input("Qual item deseja adicionar a sua lista? ")
        Lista_de_compras.append(item)
        print(f"'{item}' Acaba de ser adicionado a sua lista!")

    elif escolha == '2':
        print("\n--- Sua Lista de Compras ---")
        if not Lista_de_compras:
            print("Sua lista está vazia...")
        else:
            for i, item in enumerate(Lista_de_compras):
                print(f"{i + 1}. {item}")
        print("----------------------------")

    elif escolha == '3':
        if not Lista_de_compras:
            print("Sua lista de compras está vazia.")
        else:
            print("\n---> Itens para remover <---")
            for i, item in enumerate(Lista_de_compras):
                print(f"{i + 1}. {item}")
            print("----------------------------")

            try:
                num_item = int(input("Digite o número de um item que você deseja remover: "))
                indice_remover = num_item - 1

                if 0 <= indice_remover < len(Lista_de_compras):
                    item_removido = Lista_de_compras.pop(indice_remover)
                    print(f"'{item_removido}' foi removido da sua lista.")
                else:
                    print("Erro: Número fora do alcance. Digite um número que esteja na lista.")

            except ValueError:
                print("Erro: Entrada inválida. Digite um **número**.")

    else:
        print("Opção inválida. Digite um número que esteja no menu.")