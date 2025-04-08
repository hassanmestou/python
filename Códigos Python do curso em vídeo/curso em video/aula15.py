#n = s = 0
#while True:
    #n = int(input('Digite um número: '))
    #if n == 999:
      #  break
    #s += n
# print('A soma vale {}'.format(s))
#print(f'A soma vale {s}')

n = senha = 0
while True:
    n = str(input('Digite o seu nome: '))
    senha = int(input('Digite a senha: '))
    if n == 'Hassan' and senha == 1234:
        break
print(f'bem vindo {n}')
print('Acabou')
