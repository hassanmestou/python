from random import randint
import time
itens = ('pedra', 'papel', 'tesoura')
computer = randint(0, 2)
print(''''Opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
escolha = int(input('Qual opção você vai escolher: '))
time.sleep(1)
print('JO')
time.sleep(2)
print('KEN')
time.sleep(3)
print('PO!!!!!!')
print('-=' * 10)
print('Computador jogou {}'.format(itens[computer]))
print('jogador jogou {}'.format(itens[escolha]))
print('-=' * 10)
if computer == 0:
    if escolha == 0:
        print('EMPATE')
    elif escolha == 1:
        print('jogador vence')
    elif escolha == 2:
        print('computador vence')
    else:
        print('Opção invalida')
elif computer == 1:
    if escolha == 0:
        print('COMPUTADOR VENCE')
    elif escolha == 1:
        print('EMPATE')
    elif escolha == 2:
        print('JOGADOR VENCE')
    else:
        print('OPÇÃO invalida')
elif computer == 2:
    if escolha == 0:
        print('JOGADOR VENCE')
    elif escolha == 1:
        print('COMPUTADOR GANHA')
    elif escolha == 2:
        print('EMPATE')
    else:
        print('Opção invalida')
