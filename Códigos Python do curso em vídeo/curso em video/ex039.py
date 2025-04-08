from datetime import date
atual = date.today().year
idade = atual - ano
print('-=-' * 10)
print('ALISTAMETO MILITAR')
print('-=-' * 10)
ano = int(input('Qual o ano que você naceu: '))
if idade == 2004:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria já ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
