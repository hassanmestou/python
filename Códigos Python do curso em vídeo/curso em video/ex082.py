num = []
par = []
imp = []
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 == 1:
        imp.append(n)
    s = str(input('Quer continuar [S/N]: '))
    if s in 'Nn':
        break
print('Os valores foram: ')
print(num)
print('Os valores pares foram: ')
print(par)
print('os valores impares foram: ')
print(imp)
