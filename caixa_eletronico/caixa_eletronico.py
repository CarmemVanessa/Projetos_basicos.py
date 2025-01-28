saldo = 0.0

def menu():
    print('CAIXA ELETRONICO: ')
    print('''
          1- Realizar Deposito
          2- Realizar Saque
          3- Ver Saldo
          4- Sair
          ''')

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print('Foi adicionado a sua conta o valor de R${valor:.2f} reais')
    else:
        print('Valor invalido')
        
def saque(valor):
    global saldo
    if 0 < valor < saldo:
        saldo -= valor
        print('Foi retirado da sua conta o valor de R${valor:.2f} reais')
    else:
        print('saldo insuficiente para saque. ')

def ver_saldo():
    print(f'Seu saldo atual é R${saldo:.2f} reais')
        

    
while True:
    menu()
    opção = int(input('Escolha uma opção: '))
    
    if opção == 1:
        valor = float(input("Qual valor deseja depositar em sua conta?: "))
        deposito(valor)
    
    elif opção == 2:
        valor = float(input('Qual valor deseja retirar da sua conta?: '))
        saque(valor)
    
    elif opção == 3:
        ver_saldo()
    
    elif opção == 4:
        print('Encerrando o caixa....')
        break
    
    else:
        print('opção invalidade!')
        print('Escolha uma opção valida.')
        
        
        