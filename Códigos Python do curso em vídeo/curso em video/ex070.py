soma = caro = conta = menor = 0
print('-'*20)
print('\033[4;35mLoja ghost360\033[m')
print('-'*20)
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Qual o preço:R$ '))
    soma += preço
    conta += 1
    continua = ' '
    if preço > 1000:
        caro += 1
    if conta == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continua == 'N':
        break
print('-=-=-=-\033[4;31mfim do programa\033[m-=-=-=--=-')
print(f'A soma dos produtos, de sua compra é {soma:.2f}')
print(f'A quantidade de valores mais altos do que 1000 é R${caro}')
print(f'O menor produto é {barato} e o seu preço e de {menor:.2f}')
