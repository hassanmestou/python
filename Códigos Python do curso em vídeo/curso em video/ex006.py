n = int(input('digite um numero qualquer para saber seu dobro, triplo e a sua raiz quadrada '))
d = n ** 2
t = n ** 3
rq = n**(1/2)
print('o dobro do numero \033[0;34m{}\033[m é \033[7;34;40m{}\033[m'.format(n, d))
print('o triplo do numero \033[0;34m{}\033[m é \033[7;36;40m{}\033[m'.format(n, t))
print('a raiz quadrada do numero \033[1;35m{}\033[m \033[31mé igual a\033[m \033[4;36;40m{}\033[m!'. format(n, rq))


