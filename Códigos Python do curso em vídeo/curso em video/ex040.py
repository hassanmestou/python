nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
c = (nota + nota2) / 2
valor = c // 2
if c <= 4.9:
    print('\033[31mVocê está reprovado\033[m')
    print('\033[35mTente melhorar\033[m')
elif c == 5 or valor <= 6:
    print('\033[33mVocê está de recuperação, por sua média estar {}\033[m'.format(c))
    print('\033[36mAproveite a oportunidade\033[m')
elif c >= 7:
    print('\033[32mA pessoa que tirou {} e na segunda nota {}, a media será de {}\033[m'.format(nota, nota2, c))
    print('\033[33mAprovado\033[m')

