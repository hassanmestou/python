import time
n = float(input('diga o primeiro numero: '))
n2 = float(input(' diga a outra nota'))
s = n + n2
rf = s / 2
t = time.time_ns()
print('carregando resultados')
print('a media será \033[4;34m{}'.format(rf))

