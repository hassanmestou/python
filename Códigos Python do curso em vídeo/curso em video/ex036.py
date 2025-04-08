vdc = float(input('o valor da casa por favor: '))
salario = float(input('Seu salario por favor: '))
anos = int(input('digite em quantos anos voce vai pagar: '))
p = vdc / (anos * 12)
m = salario * 30 / 100
print('para pagar uma casa de R${:.2f} em {} anos'.format(vdc, anos), end='')
print(' a prestação será de R${:.2f}'.format(p))
if p <= m:
    print('\033[32mEmprestímo pode ser concedido\033[m')
else:
    print('\033[31mEmprestimo NEGADO\033[m')



