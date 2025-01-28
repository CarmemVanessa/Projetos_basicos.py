import random

opções = ['pedra', 'papel', 'tesoura']

escolha_jogador = input("escolha Pedra, Papel, Tesoura: ").lower()

escolha_computador = random.choice(opções)
print(f'O computador escolheu: {escolha_computador}')

if escolha_jogador == escolha_computador:
    print("Empate!")
elif escolha_jogador == 'pedra' and escolha_computador == 'tesoura' or \
    escolha_jogador == 'papel' and escolha_computador == 'pedra' or \
    escolha_jogador == 'tesoura' and escolha_computador == 'papel':
        print("Você venceu!")
else:
    print("Você perdeu")
    