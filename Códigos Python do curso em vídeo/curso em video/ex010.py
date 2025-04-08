d = int(input('diga quanto de dinheiro você tem, para saber quantos dolares pode comprar: '))
D = d / 3.27
print('/'*20)
print('você poderá comprar \033[4;35m{:.2f}\033[m dolares'.format(D))
print('/'*20)
