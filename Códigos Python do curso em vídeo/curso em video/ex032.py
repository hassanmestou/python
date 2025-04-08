ano = int(input('Digite um ano para saber se ele é bissexto: '))
if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    print('\033[35mo ano é bissexto\033[m')
else:
    print('\033[34mo ano não é bissexto\033[m')

