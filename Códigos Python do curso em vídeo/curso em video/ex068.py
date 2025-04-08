import random
print('=-'*20)
print('vamos jogar par ou impar')
print('=-'*20)
v1 = v2 = par = impar = pi = 0
while True:
    n = random.randint(0, 10)
    num = int(input('Digite um número: '))
    while pi != 'PI':
        pi = str(input('Digite se é [P/I]: ')).strip().upper()[0]
        if pi in 'IP':
            break
    print('-'*20)
    soma = n + num
    print(f'Você digitou {num} e eu {n}. A soma total é {soma}',end=' ')
    print('deu par' if soma % 2 == 0 else 'deu impar')
    if soma % 2 == 1 and pi == 'P':
        v2 += 1
        print('Computador ganhou')
        break
    if soma % 2 == 0 and pi == 'P':
        v1 += 1
        print('Você ganhou')
    if soma % 2 == 1 and pi == 'I':
        v1 += 1
        print('Você ganhou')
    if soma % 2 == 0 and pi == 'I':
        v2 += 1
        print('Computador ganhou')
        break
    print('-'*20)
    print('Vamos jogar de novo.....')
print(f'Você perdeu a partida, suas vitorias {v1} ')
print('-=-' * 30)

