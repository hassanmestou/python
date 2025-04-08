from math import floor
nome = float(input('\033[31mdiga um numero real\033[m: '))
c = floor(nome)
print('\033[37ma parte inteira do numero\033[m \033[4;31m{}\033[m é \033[4;36m{}'.format(nome, floor(nome)))
