cores = {'limpa':'\033[m',
         'amarela':'\033[33m',
         'azul':'\033[34m',
         'nãosei':'\033[7;34;33m',
         'azulsublinhadacomtraçovermelho':'\033[7;36m'}
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro valor :'))
num3 = int(input('Digite outro valor: '))
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor =num3
# verificando
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('{}o menor valor digitado foi{} {}{}{}'.format(cores['amarela'], cores['limpa'], cores['nãosei'], menor, cores['limpa']))
print('o maior valor digitado  foi {}{}{}'.format(cores['azulsublinhadacomtraçovermelho'], maior, cores['limpa']))








    


