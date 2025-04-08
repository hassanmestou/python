velocidade  = float(input('digite a velocidade do carrro: '))
calculo = 80 - velocidade
c = 7 * calculo
if velocidade >= 80:
    print('\033[31matenção\033[m: \033[33mvocê ultrapassou do limite que é 80km você receberá, uma multa de {:.1f}\033[mR$'.format(c))
else:
    print('\033[32mok está tudo certo, dirija com cuidado\033[m')