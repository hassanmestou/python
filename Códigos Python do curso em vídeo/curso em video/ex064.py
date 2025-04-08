n = count = c2 = 0
n = int(input('Digite um número:[999 para parar] '))
while n != 999:
    c2 += n
    count += 1
    n = int(input('Digite um número:[999 para parar] '))
print('A quantidade de valores é {} e a soma entre eles {}'.format(count, c2))


