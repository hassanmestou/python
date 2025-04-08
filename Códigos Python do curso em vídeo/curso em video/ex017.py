cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'azulpreto': '\033[7;36m'}
from math import sqrt
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
cco = co**2
cca = ca**2
s = cca+cco
cf1 = sqrt(s)
print('a hipotenusa vai medir {}{:.2f}{}'.format(cores['azulpreto'], cf1, cores['limpa']))

