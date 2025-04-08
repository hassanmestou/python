frase = str(input('escreva uma frase: ')).upper()
n = frase.count('A')
b = frase.find('A')
# n = frase.upper().find('A')
print('\033[36ma frase tem\033[m \033[4;33m{}\033[m \033[36ma\033[m'.format(n))
print('\033[34ma primeira palavra está na posicao\033[m \033[4;32m{}\033[m'.format(b))
print('\033[33ma ultima palavra está na parte\033[m \033[4;31m{}\033[m'.format(frase.rfind('A')))

