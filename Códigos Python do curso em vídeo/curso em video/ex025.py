nome = str(input('Diga o seu nome: '))
cf = nome.upper()
print('\033[31msilva tem no nome\033[m \033[4;36m{}\033[m'.format('SILVA' in cf))
