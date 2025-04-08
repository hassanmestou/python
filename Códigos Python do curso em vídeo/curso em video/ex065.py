num = count = soma = div = maior = menor = 0
r = 'S'
while r != 'N':
    num = int(input('Digite um número: '))
    r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    count += 1
    soma += num
    div = soma / count
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('O maior valor é {} e o menor é {}'.format(maior, menor))
print('A quantidade de valores foi {} e a média entre eles foi de {:.1f}'.format(count, div))

