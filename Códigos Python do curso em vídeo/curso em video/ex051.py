print('='*20)
print('10 primeiros termos na P.A')
print('='*20)
n1 = int(input('O primeiro termo: '))
n = int(input('Qual a razão: '))
for c in range(n1, n1 + (9*n) + n, n):
    print(c, end=' -> ')
print('acabou')
