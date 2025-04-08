sexo = c = maiores = 1
v = man = woman = 0
while True:
    print('-=-' * 20)
    print('Meu cadastro')
    print('-=-' * 20)
    idade = int(input('Qual a sua idade: '))
    if idade > 18:
        v += 1
    while sexo != 'MF':
        sexo = str(input('Qual o seu sexo: ')).upper().strip()[0]
        if sexo in 'MF':
            break
    if sexo == 'M':
        man += 1
    print('-'*10)
    if sexo == 'F' and idade < 20:
        woman += 1
    while c != 'SN':
        c = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if c in 'SN':
            break
    if c in 'N':
        break
print('\033[31m-----------\033[m\033[4;31mFim do cadastro\033[m\033[31m------------\033[m')
print(f'As pessoas com mais de 18 anos são {v}')
print(f'Temos {man} homens')
print(f'tem {woman} mulheres com menos de 20 anos')
