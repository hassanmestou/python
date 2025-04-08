nome = str(input('qual é o seu nome: '))
if nome == 'hassan':
    print('que nome bonito')
elif nome == 'pedro' or nome == 'rana':
    print('seu nome é popular no brazil ')
elif nome in 'ana claudia jessica blala':
    print('belo nome feminino')
elif nome in 'homem hassan':
    print('Belo nome masculino ')
print('bom dia'.format(nome))
