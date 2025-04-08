from datetime import date
s = date.today().year
d = 0
f = 0
tot = 0
tot2 = 0
for c in range(1, 7+1):
    ano = int(input('Digite a {} pessoa do seu ano de nacimento: '.format(c)))
    ano += 1
    f = s - ano
    if f >= 21:
        tot += 1
    else:
        tot2 += 1
print('A quantidade de pessoas velhas é {}'.format(tot))
print('E a quantidade de pessoas novas é {}'.format(tot2))


