n = count = cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    count += n
    cont += 1
print(f'A quantidade de valores digitados foi {cont} e a soma entre eles é {count}')
