salario = float(input('Qual é o seu salario:R$ '))
if salario >= 1250:
    c = (salario * 10)//100
    s = salario + c
    print('\033[7;31;39mo seu aumento foi de\033[m \033[4;36mR${}\033[m'.format(s))
else:
    n = (salario * 15)//100
    f = salario + n
    print('\033[7;39mo seu salario foi de R${}\033[m'.format(f))
print('\033[4;33mparabens\033[m')
