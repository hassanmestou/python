cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'azulclaro':'\033[36m',
         'vermelho':'\033[31m'}
distancia = float(input('digite qual e a distancia em quilometros: '))
c = (distancia)*0.45
d = (distancia)*0.50
if distancia >= 200:
    print('{}você passou de 200km o novo valor será 0.45 o preço que você deverá pagar será de {}{}R$'.format(cores['vermelho'], c, cores['limpa']))
else:
    print('{}você começou uma viagem de {}{}Km'.format(cores['amarelo'], distancia, cores['limpa']))
    print('{}você pagará {:.2f}{}'.format(cores['azulclaro'], d, cores['limpa']))
