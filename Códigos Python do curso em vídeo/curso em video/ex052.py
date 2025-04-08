n = int(input('Digite um número: '))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divísivel {} vezes'.format(n, count))
if count == 2:
    print('E por isso ele primo')
else:
    print('E por isso ele não é primo')


    



