#cores
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
s = float(input('diga qual é o salrio do funcíonario:R$ '))
c = 1+0.15
cf = c*s
print('o funcionario agora receberá {}{:.2f}R${}'.format(cores['amarelo'], cf, cores['limpa']))
