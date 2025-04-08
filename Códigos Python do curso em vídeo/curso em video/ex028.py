cores = {'limpa':'\033[m', 'amarelo':'\033[33m', 'azulclaro':'\033[36m', 'verde':'\033[32m'}
import random
n = random.randint(0, 5)
usuario = int(input('Qual o numero que você acha: '))
if usuario == n:
    print('{}você acertou, parabens{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}Mais sorte da proxima vez{}'.format(cores['amarelo'], cores['limpa']))





