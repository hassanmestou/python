num = []
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Número cadastrado')
    else:
        print('Valor está em números')
    r = str(input('Quer continuar [S/N]: '))
    if r in 'nN':
        break
print(f'Os números foram {num}')