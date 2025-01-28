agenda = []

def adicionar_contato(nome, telefone):
    contatos = {"nome": nome,  "telefone": telefone}
    agenda.append(contatos)
    print(f"Contato {nome} adiciona com sucesso")
    
def remover_contato(nome):
    for contato in agenda:
        if contato["nome"] == nome:
            agenda.remove(contato)
            print(f'contato {nome} ecluido com sucesso')
            return
        
    print(f'contato de {nome} não encontrado!')

def buscar_contato(termo):
    resultado = []
    for contato in agenda:
        if termo in contato["nome"] or contato["telefone"]:
            resultado.append(contato)
    
    if resultado:
        print('contatos encontrados!')
        for contato in resultado:
            print(f'Nome: {contato["nome"]}, Telefone {contato["telefone"]}')
    else:
        print("contatos não encontrados!")

def exibir_contatos():
    if agenda:
        print("Lista de contatos:")
        for contato in agenda:
            print(f'Nome:, {contato["nome"]}, Telefone: {contato['telefone']}')
    else:
        print("Agenda vazia")
    
def exibir_menu():
    print("\nMENU")
    print("1 - Adicionar contatos")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Exibir lista de contatos")
    print("5 - Sair")
    
def agenda_contatos():
    while True:
        exibir_menu()
        opção = input("Escolha uma opção: ")
        
        if opção == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            adicionar_contato(nome, telefone)
        
        elif opção == "2":
            nome = input("Digite o nome do contato que deseja remover: ")
            remover_contato(nome)
        
        elif opção == "3":
            termo = input(" Digite o nome ou telefone que deseja procurar na sua agenda: ")
            buscar_contato(termo)
        
        elif opção == "4":
            exibir_contatos()
            
        elif opção == "5":
            print("Encerrando programa....")
            break
        
        else:
            print("Opção invalida!")
        
agenda_contatos()
             
    