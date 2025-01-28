tarefas = []
tarefas_concluidas = []

def adicionar_tarefa(titulo, descrição):
    tarefa = {"titulo": titulo, "descrição": descrição}
    tarefas.append(tarefa)
    print("Atividade adicionada com sucesso! ")
    
    
def remover_tarefas(titulo):
    for tarefa in tarefas:
        if tarefa["titulo"] == titulo:
            tarefas.remove(tarefa)
            print(f"tarefa {titulo} adicionada com sucesso")
            return
    else:
            print(f"tarefa {titulo} não encontrada")
        
def concluir_tarefa(titulo):
    for tarefa in tarefas:
        if tarefa['titulo'] == titulo:
            tarefas_concluidas.append(tarefa)
            tarefas.remove(tarefa)
            print(f"tarefa {titulo} marcada como concluida!")
            return
    else:
            print(f"Tarefa {titulo} não encontrada!")
    
def exibir_tarefas():
    print("\nTAREFAS PENDENTES")
    for tarefa in tarefas:
        print(f"tarefa: {tarefa["titulo"]}\nDescrição: {tarefa["descrição"]}\n")
        
    print("\nTAREFAS CONCLUIDAS")
    for tarefa in tarefas_concluidas:
        print(f"tarefa: {tarefa["titulo"]}\nDescrição: {tarefa["descrição"]}\n")
        

def menu():
    while True:
        print("\nMENU")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefas")
        print("3 - Marca tarefa como concluida")
        print("4 - Exibir tarefas")
        print("5- sair")
        
        opção = input("Digite a opção desejada: ")
        
        if opção == "1":
            titulo = input("Digite o titulo da tarefa: ")
            descrição = input("Escreva a descrição da tarefa: ")
            adicionar_tarefa(titulo, descrição)
        
        elif opção == "2":
            titulo = input("Dgite o titulo da tarefa a ser removida: ")
            remover_tarefas(titulo)
            
        elif opção == "3":
            titulo = input("Qual o titulo da tarefa que deseja marcar como concluida: ")
            concluir_tarefa(titulo)
        
        elif opção == "4":
            exibir_tarefas()
            
        elif opção == "5":
            print("Incerrando o gerenciamento de tarefas...")
            break
        
        else:
            print("Opção invalida!")
            
menu()
                
    
    
