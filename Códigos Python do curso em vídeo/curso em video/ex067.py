while True:
    num = int(input('Digite um numero: '))
    print('-' * 20)
    if num < 0:
        break
    for c in range(0, 11):
        c += 1
        count = num * c
        print(f'{num} X {c} = {count}')
    print('-' * 20)
print('Programa encerrado, volte quando quiser')
