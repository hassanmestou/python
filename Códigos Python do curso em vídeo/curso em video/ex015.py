cores = {'limpa':'\033[m', 'azul':'\033[34m'}
a = float(input('\033[31mPor quantos dias você alugou o carro\033[m: '))
km = float(input('\033[31mPor quantos quilometros o carro rodou\033[m: '))
aluguel = a*60
Km = km*0.15
cf = aluguel+Km
print('o valor total que você precisará pagar é {}{}{}R$'.format(cores['azul'], cf, cores['limpa']))




