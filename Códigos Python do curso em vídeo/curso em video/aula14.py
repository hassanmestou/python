'''n = 1
s = 1
while n != 'M' or n != 'F':
    n = str(input('Digite o seu sexo:[M/F] ')).upper()'''

n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
l = ['tot', 0, 'n', 1, 'n3', 1]
escolha = 1
while escolha != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior valor')
    print('[4] novos números')
    print('[5] sair do programa')
    escolha = int(input('>>>> Qual das opções: '))
    if escolha == 1:
        print('a soma dos valores é {} e {} é {}'.format(n1, n2, n1 + n2))
    if escolha == 2:
        print('a multiplicação dos valores de {} e {} é {}'.format(n1, n2,n1 * n2))
    if escolha == 3:
        if n1 < n2:
            tot = n2
        elif n1 > n2:
            tot = n1
        print('O maior valor é {}'.format(tot))




