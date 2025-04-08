tot1 = 0
tot2 = 0
for peso in range(1, 5+1):
    pe = float(input('Digite o peso da {} pessoa: '.format(peso)))
    if peso == 1:
        tot1 = pe
        tot2 = pe
    else:
        if pe > tot1:
            tot1 = pe
        if pe > tot1:
            tot2 = pe
print('o maior valor é {}')




