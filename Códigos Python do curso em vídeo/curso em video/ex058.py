print('sou seu computador... pensei em um número entre 0 e 10 qual é!: ')
from random import randint
números = randint(0, 10)
s = 0
n = 1
while n != números:
    n = int(input('Qual o seu palpite: '))
    s += 1
    if n < números:
        print('mais.... tente de novo')
    elif n > números:
        print('menos...')
print('Você ganhou, mas foi necessario {} palpites para você acertar!'.format(s))
