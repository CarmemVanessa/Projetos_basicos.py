# Bem vindo ao meu sistema de um diario virtual
# Será necesario importar um modulo 


def menu_principal(): 
    print('''
-------Meu diario virtual-------
1 - Adicionar mais uma pagina ao meu diario.
2 - Ver Paginas.
3 - Listar Paginas
4 - Excluir Paginas
5 - Sair
''')
    
Diario = [] # Lista para armazenar as paginas do diario

def adicionar_pagina(Diario, titulo, conteudo):
    # função especifica para adicionar uma nova pagina ao diario virtual
    # adicionei uma nova função: colocar titulo nas paginas
    from datetime import datetime
    entrada = {
        'titulo': titulo,
        'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'conteudo': conteudo
         }
    Diario.append(entrada)
    print('Pagina adiciona com sucesso! ')
    
   

def ver_paginas(Diario, titulo):
    # função especifica para percorrer os diario
    for entrada in Diario:
        if entrada['titulo'] == titulo:
                print(f"Título: {entrada['titulo']}\nData: {entrada['data_hora']}\nConteúdo: {entrada['conteudo']}")
                return
    print('Pagina não encontrada! ')

def listar_paginas(Diario):
    if not Diario:
        print('o Diario esta vazio!')
    else:
        print('-------Titulos disponiveis------')
        for i, entrada in enumerate(Diario):
            print(f'{i + 1}. {entrada['titulo']}')

def exclui_pagina(Diario, titulo):
    for entrada in Diario:
        if entrada['titulo'] == titulo:
            Diario.remove(entrada)
            print('Pagina excluida com sucesso! ')
            return
    print('Pagina não encontrada! ')
    
   

while True:
    menu_principal()
    escolha = input('escolha uma opção: ')
    
    if escolha == '1':
        titulo = input('Titulo: ')
        conteudo = input('Conteudo: ')
        adicionar_pagina(Diario, titulo, conteudo)
    elif escolha == '2':
        titulo = input('Digite o titulo da pagina: ')
        print('')
        ver_paginas(Diario, titulo)
    elif escolha == '3':
        listar_paginas(Diario)
    elif escolha == '4':
        titulo = input('Digite o titulo da pagina: ')
        exclui_pagina(Diario,titulo)
    elif escolha == '5':
        print('Fechando seu diario! Até logo..')
        break
    else:
        print('Opção Invalida. Tente Novamente! ')
        
            
    


