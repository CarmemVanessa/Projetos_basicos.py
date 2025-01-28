def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

def exponenciar(x, y):
    return x ** y

def exibir_menu():
    print("Selecione a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Exponenciar")
    print("6 - Exibir histórico")
    print("7 - Limpar histórico")
    print("8 - Sair")

def calculadora():
    historico = []

    while True:
        exibir_menu()
        escolha = input("Digite a opção desejada (De 1 a 8): ")

        if escolha == "8":
            print("Encerrando a calculadora...")
            break

        if escolha in ["1", "2", "3", "4", "5"]:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            
            if escolha == "1":
                resultado = adicionar(numero1, numero2)
                operacao = f"{numero1} + {numero2} = {resultado}"

            elif escolha == "2":
                resultado = subtrair(numero1, numero2)
                operacao = f"{numero1} - {numero2} = {resultado}"

            elif escolha == "3":
                resultado = multiplicar(numero1, numero2)
                operacao = f"{numero1} * {numero2} = {resultado}"

            elif escolha == "4":
                resultado = dividir(numero1, numero2)
                operacao = f"{numero1} / {numero2} = {resultado}"

            elif escolha == "5":
                resultado = exponenciar(numero1, numero2)
                operacao = f"{numero1} ** {numero2} = {resultado}"

            else:
                print("Opção inválida!")
                continue

        elif escolha == "6":
            print("\nHistórico de Operações:")
            for operacao in historico:
                print(operacao)
            continue

        elif escolha == "7":
            historico.clear()
            print("Histórico limpo!")
            continue

       
        print(operacao)
        historico.append(operacao)

calculadora()
