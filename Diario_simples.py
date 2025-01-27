from datetime import datetime
# Bem vindo ao meu sistema de um diario virtual
# Será necesario importar um modulo 

class Diario_virtual:
    def __init__(self):
        self.paginas = []
    
    def adicionar_pagina(self, titulo, conteudo):
    # função especifica para adicionar uma nova pagina ao diario virtual
    # adicionei uma nova função: colocar titulo nas paginas
        entrada = {
            'titulo': titulo,
            'data_hora': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'conteudo': conteudo
            }
        self.paginas.append(entrada)
        print('Pagina adiciona com sucesso! ')
        
    def ver_paginas(self, titulo):
    # função especifica para percorrer os diario
        for entrada in self.paginas:
            if entrada['titulo'] == titulo:
                    print(f"Título: {entrada['titulo']}\nData: {entrada['data_hora']}\nConteúdo: {entrada['conteudo']}")
                    return
        print('Pagina não encontrada! ')
    
    def listar_paginas(self):
        if not self.paginas:
            print('o Diario esta vazio!')
        else:
            print('-------Titulos disponiveis------')
            for i, entrada in enumerate(self.paginas):
                print(f'{i + 1}. {entrada['titulo']}')
                
    def exclui_pagina(self, titulo):
        for entrada in self.paginas:
            if entrada['titulo'] == titulo:
                self.paginas.remove(entrada)
                print('Pagina excluida com sucesso! ')
                return
            
    def menu_principal(self):
        while True:
            
            print('Pagina não encontrada! ')
            print('''
        -------Meu diario virtual-------
        1 - Adicionar mais uma pagina ao meu diario.
        2 - Ver Paginas.
        3 - Listar Paginas
        4 - Excluir Paginas
        5 - Sair
        ''')
            
            escolha = input("Digite uma escolha: ")
            
            if escolha == '1':
                titulo = input('Titulo: ')
                conteudo = input('Conteudo: ')
                self.adicionar_pagina(titulo, conteudo)
            elif escolha == '2':
                titulo = input('Digite o titulo da pagina: ')
                print('')
                self.ver_paginas(titulo)
            elif escolha == '3':
                self.listar_paginas()
            elif escolha == '4':
                titulo = input('Digite o titulo da pagina: ')
                self.exclui_pagina(titulo)
            elif escolha == '5':
                print('Fechando seu diario! Até logo..')
                break
            else:
                print('Opção Invalida. Tente Novamente! ')

if __name__ == "__main__":
    meu_diario = Diario_virtual()
    meu_diario.menu_principal()
                
                
    



    
   




    
   


   