print('-'*20)
print('Banco \033[31mghost360\033[m')
print('-'*20)
valor = int(input('Qual o valor que você quer retirar: '))
conta = valor
ced = 50
total = 0
while True:
    if conta >= ced:
        conta -= ced
        total += 1
    else:
        print(f'Você vai receber {total} notas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total = 0
        if total == 0:
            break

