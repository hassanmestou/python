print('gerador de P.A')
print('-=-'*10)
n = int(input('Qual o número por onde você quer começar: '))
razao = int(input('Qual a razão: '))
c = 1
total = 0
s = 10
while s != 0:
    total += s
    while c <= 10:
        print('{}'.format(n), end=' --> ')
        n += razao
        c += 1
    s = int(input('Quantos mais você quer: '))
    print('pausa')
print('FIM')

