cores = {'limpa':'\033[m',
         'azul':'\033[4;34m',
         'vermelho':'\033[4;31m'}
#segmentos
print('=-'*20)
print('analisador de triangulos: ')
print('=-'*20)
p = float(input('qual é a primeira medida: '))
p2 = float(input('qual é a sgunda medida: '))
p3 = float(input('qual é o terceira medida: '))
if p < p2 + p3 and p2 < p3 + p and p3 < p2 + p:
    print('{}a medida pode formar um triangulo:{} '.format(cores['azul'], cores['limpa']))
else:
    print('{}a medida nao pode formar um triangulo{}'.format(cores['vermelho'], cores['limpa']))
