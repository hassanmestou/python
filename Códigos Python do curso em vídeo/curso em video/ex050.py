s = 0
c = 0
for c in range(0, 7):
    n = int(input('digite um número: '))
    if n % 2 == 0:
        s += n
        c = c + 1
print('A soma dos valores pares é {}'.format(s))



