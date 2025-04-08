frase = str(input('Digite uma frase: ')).upper()
fras = frase.replace(" ","")
de = fras[::-1]
for frase in range(0, 1):
    print('o inverso da palavra {} é {}'.format(fras, de), end=' ')
    if fras == de:
         print('\nEla é um polindromo')
    else:
        print('\nEla não é um polindromo')
