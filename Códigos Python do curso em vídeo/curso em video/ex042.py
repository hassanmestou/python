#if p < p2 + p3 and p2 < p3 + p and p3 < p2 + p
print('-=-'*20)
print('ANALISADOR DE TRIANGULOS E CLASSIFICADOR')
print('-=-'*20)
m = float(input('Digite o primeiro angulo: '))
m1 = float(input('Digite o segundo angulo: '))
m2 = float(input('Digite o terçeiro angulo: '))
if m < m1 + m2 and m1 < m2 + m and m2 < m1 + m:
    print('Os seguimentos podem formar um triângulo',end=' ')
    if m == m1 and m1 == m2 and m == m2:
       print('EQUILáTERO')
    elif m != m1 != m2 != m:
        print('ESCALENO')
    else:
        print('ISÒSCELES')
else:
    print('Não vai formar um triangulo')



