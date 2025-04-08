princ = []
geral = []
mai = men = 0
while True:
    geral.append(str(input('Digite o seu nome: ')))
    geral.append(float(input('Qual o seu peso: ')))
    if len(geral) == 0:
        mai = men = geral[1]
    else:
        if geral[1] < mai:
            mai = geral[1]
        if geral[1] > men:
            men = geral[1]
    princ.append(geral[:])
    geral.clear()
    continua = str(input('Quer continuar a escrever: '))
    if continua in 'Nn':
        break
print(f'As pessoas registradas foram {princ}')
print(f'A pessoa mais pesada é {mai}')
print(f'A pessoa menos pesada é {men}')
