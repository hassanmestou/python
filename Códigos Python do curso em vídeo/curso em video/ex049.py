s = 0
numero = int(input('Digite o número para saber sua tabuada: '))
for n in range(0, 11, 1):
    print('{} x {} = {}'.format(numero, n, numero * n))
    print(n)

