lista_compras = []

def exibir_menu():
    print('''
          \nMENU: 
          1- Adicionar itens a lista
          2- Remover itens a lista
          3- Exibir a lista completa de compras
          4- Sair
          ''')

def adicionar_item():
    item = input("Digite o nome do item: ").upper()
    lista_compras.append(item)
    print(f"Item {item} adicionado com sucesso!!!")

def remover_item():
    item = input("Digite o item a ser removido da lista: ").upper()
    if item in lista_compras:
        lista_compras.remove(item)
        print(f"item {item} removido com sucesso!!!")
    else:
        print("esse item não esta na lista de compras")

def mostrar_lista():
    if len(lista_compras) == 0:
        print("Sua lista de compras esta vazia")
    else:
        print('LISTA DE COMPRAS:')
        for item in lista_compras:
            print(item)
    
while True:
    exibir_menu()
    opção = input("Escolha uma opção (0 para sair): ")
    
    if opção == "1":
        adicionar_item()
    elif opção == "2":
        remover_item()
    elif opção == "3":
        mostrar_lista()
    elif opção == "4":
        print("Fechando programa...3, 2, 1")
        break
    else:
        print("Opção invalidade \nDigite uma opção valida!")


