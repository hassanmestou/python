cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azulclaro':'\033[36m'}
import random
al = input('primeiro aluno: ')
ab = input('o segundo aluno: ')
ac = input('o terceiro aluno: ')
l = [al, ab, ac]
sorteio = random.choice(l)
print('o aluno escolhido foi o {}{}{}'.format(cores['azulclaro'], sorteio, cores['limpa']))




