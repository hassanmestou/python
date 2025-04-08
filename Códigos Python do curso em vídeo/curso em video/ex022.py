cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'vermelho':'\033[31m',
         'azulclaro':'\033[4;36m'}
nome = str(input('qual é o seu nome: ')).strip()
print('seu nome em letras maisculas {}{}{}'.format(cores['vermelho'], nome.upper(), cores['limpa']))
print('seu nome em minusculo {}{}{}'.format(cores['amarelo'], nome.lower(), cores['limpa']))
print('seu nome tem tantas {}{}{} letras'.format(cores['vermelho'], len(nome) - nome.count(' '), cores['limpa']))
dividido = nome.split()
print('seu nome tem {}{}{} letras'.format(cores['amarelo'], len(dividido[0]), cores['limpa']))
