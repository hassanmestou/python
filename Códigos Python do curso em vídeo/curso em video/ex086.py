matriz = [[0, 0 ,0], [0, 0, 0],[0, 0, 0]]
spar = somat = scol = 0
mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}, {c}]: '))
print('-=' *30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    somat += matriz[l][2]
    print()
print('-=' * 30)
print(f'A soma dos valores pares são {spar}')
print(f'a soma dos valores da terceira coluna é {somat}')
for c in range(0, 3):
    if c == 0:
        matriz[1][c] = mai
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f'O maior da linha 2 é {mai}')


