from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
escolha = 0
tot = 0
total = 0
escolha2 = 1
while escolha != 5:
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior valor')
    print('[4] novos números')
    print('[5] sair do programa')
    escolha = int(input('>>>> Qual das opções: '))
    if escolha == 1:
        print('a soma dos valores é {} e {} é {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('a multiplicação dos valores de {} e {} é {}'.format(n1, n2,n1 * n2))
    elif escolha == 3:
        if n1 < n2:
            tot = n2
        elif n1 > n2:
            tot = n1
        print('O maior valor é {}'.format(tot))
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('segundo valor: '))
    elif escolha == 5:
        print('Finalizando....')
    sleep(2)
    print('-=-'*10)
print('Obg, volte sempre')
