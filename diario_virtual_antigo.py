# Bem-vindo ao meu sistema de um diário virtual
# Será necessário importar um módulo

def menu_principal():
    print('''
-------Meu Diário Virtual-------
1 - Adicionar mais uma página ao meu diário
2 - Ver Páginas
3 - Listar Páginas
4 - Excluir Páginas
5 - Sair
''')

Diario = []  # Lista para armazenar as páginas do diário

def adicionar_pagina(Diario, titulo, conteudo):
    # Função específica para adicionar uma nova página ao diário virtual
    # Agora é possível adicionar títulos às páginas
    from datetime import datetime
    entrada = {
        "titulo": titulo,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "conteudo": conteudo
    }
    Diario.append(entrada)
    print("Página adicionada com sucesso!")

def ver_paginas(Diario, titulo):
    # Função para visualizar uma página específica pelo título
    for entrada in Diario:
        if entrada["titulo"] == titulo:
            print(f"Título: {entrada['titulo']}\nData: {entrada['data_hora']}\nConteúdo: {entrada['conteudo']}")
            return
    print("Página não encontrada!")

def listar_paginas(Diario):
    # Função para listar todas as páginas do diário
    if not Diario:
        print("O diário está vazio!")
    else:
        print("-------Títulos Disponíveis-------")
        for i, entrada in enumerate(Diario):
            print(f"{i + 1}. {entrada['titulo']}")

def exclui_pagina(Diario, titulo):
    # Função para excluir uma página pelo título
    for entrada in Diario:
        if entrada["titulo"] == titulo:
            Diario.remove(entrada)
            print("Página excluída com sucesso!")
            return
    print("Página não encontrada!")

# Loop principal para interagir com o menu
while True:
    menu_principal()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        titulo = input("Título: ")
        conteudo = input("Conteúdo: ")
        adicionar_pagina(Diario, titulo, conteudo)
    elif escolha == "2":
        titulo = input("Digite o título da página: ")
        ver_paginas(Diario, titulo)
    elif escolha == "3":
        listar_paginas(Diario)
    elif escolha == "4":
        titulo = input("Digite o título da página: ")
        exclui_pagina(Diario, titulo)
    elif escolha == "5":
        print("Fechando seu diário! Até logo...")
        break
    else:
        print("Opção inválida. Tente novamente!")
