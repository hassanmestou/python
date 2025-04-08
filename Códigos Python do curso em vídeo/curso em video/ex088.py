import random
print('-='*30)
print('{Jogo da Mega-Sena}')
print('-='*30)
lista = list()
mega = []
perg = int(input('Quantos jogos vai ser: '))
soma = 0
tot = 0
while tot + 1 <= perg:
    while True:
        n = random.randint(1, 60)
        if n not in lista:
            lista.append(n)
            soma += 1
        if soma == 6:
            break
    lista.sort()
    mega.append(lista[:])
    lista.clear()
    tot += 1
for c in range(0, perg):
    print(f'o {c} jogo é: {mega} ')



