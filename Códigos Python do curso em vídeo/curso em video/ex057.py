n = 1
s = 1
p = 1
while n != 'M' and n != 'F' and p != 'M' and p != 'F':
    n = str(input('Digite o seu sexo:[M/F] ')).strip().upper()[0]
    if n != 'M' and n != 'F' and p != 'M' and p != 'F':
        while p != 'M' and p != 'F':
            p = str(input('Dados não validos, digite novamente: ')).strip().upper()[0]
        if p == 'M' or p == 'F':
            print('Informações valídas, sexo {} anotada com sucesso'.format(p))
    else:
        print('Informações validas, sexo {} anotada com sucesso'.format(n))
