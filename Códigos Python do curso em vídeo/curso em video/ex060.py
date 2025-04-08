n1 = int(input('digite um número: '))
contador = n1
f = 1
while contador > 0:
    f *= contador
    print('{}'.format(contador),end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1
print('o valor da multiplicação é {}'.format(f), end='')


