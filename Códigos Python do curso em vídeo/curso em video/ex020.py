import random
aluno1 = input('nome do aluno 1: ')
aluno2 = input('nome do aluno 2: ')
aluno3 = input('o nome do aluno 3: ')
aluno4 = input('o nome do aluno 4: ')
l = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(l)
print('\033[33mo primeiro aluno sorteado foi\033[m \033[32m{}\033[m'.format(l))


