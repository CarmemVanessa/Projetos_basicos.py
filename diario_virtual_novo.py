from datetime import datetime

class DiarioVirtual:
    def __init__(self):
        self.paginas = []

    def adicionar_pagina(self, titulo, conteudo):
        entrada = {
            'titulo': titulo,
            'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'conteudo': conteudo
        }
        self.paginas.append(entrada)
        print('Página adicionada com sucesso!')

    def ver_pagina(self, titulo):
        for entrada in self.paginas:
            if entrada['titulo'] == titulo:
                print(f"Título: {entrada['titulo']}\nData: {entrada['data_hora']}\nConteúdo: {entrada['conteudo']}")
                return
        print('Página não encontrada!')

    def listar_paginas(self):
        if not self.paginas:
            print('O diário está vazio!')
        else:
            print('-------Títulos disponíveis------')
            for i, entrada in enumerate(self.paginas):
                print(f"{i + 1}. {entrada['titulo']}")

    def excluir_pagina(self, titulo):
        for entrada in self.paginas:
            if entrada['titulo'] == titulo:
                self.paginas.remove(entrada)
                print('Página excluída com sucesso!')
                return
        print('Página não encontrada!')

    def menu_principal(self):
        while True:
            print('''\n-------Meu Diário Virtual-------
            1 - Adicionar mais uma página ao meu diário.
            2 - Ver Página.
            3 - Listar Páginas.
            4 - Excluir Página.
            5 - Sair.
            ''')
            escolha = input('Escolha uma opção: ')

            if escolha == '1':
                titulo = input('Título: ')
                conteudo = input('Conteúdo: ')
                self.adicionar_pagina(titulo, conteudo)

            elif escolha == '2':
                titulo = input('Digite o título da página: ')
                print('')
                self.ver_pagina(titulo)

            elif escolha == '3':
                self.listar_paginas()

            elif escolha == '4':
                titulo = input('Digite o título da página: ')
                self.excluir_pagina(titulo)

            elif escolha == '5':
                print('Fechando seu diário! Até logo...')
                break

            else:
                print('Opção inválida. Tente novamente!')


# Inicializando o diário e executando o menu
if __name__ == "__main__":
    meu_diario = DiarioVirtual()
    meu_diario.menu_principal()
