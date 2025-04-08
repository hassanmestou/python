num = [[], []]
valor = 0
for k in range(0, 7):
    valor = int(input(f'Digite o {k} valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Os valores pares são {num[0]}')
print(f'Os valores impares são {num[1]}')

