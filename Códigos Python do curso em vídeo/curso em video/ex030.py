n = int(input('Digite um numero inteiro: '))
c = n % 2
if c == 0:
    print('\033[35mo numero\033[m {} \033[35mé PAR\033[m'.format(n))
else:
    print('\033[34mo numero é impar\033[m')
