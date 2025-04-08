#galera = [['joão',19],['caue', 23],['ana',13],['joaquim',14]]
#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade')


#galera = list()
#dado = list()
#totmai = totmen = 0
#for c in range(0, 3):
 #   dado.append(str(input('Nome: ')))
  #  dado.append(int(input('idade: ')))
   # galera.append(dado[:])
    #dado.clear()

#for p in galera:
 #   if p[1] >= 21:
  #      print(f'{p[0]} é maior de idade')
  #      totmai += 1
   # else:
    #    print(f'{p[0]} é menor de idade')
     #   totmen += 1
#print(f'Temos {totmai} e {totmen} pessoas menores de idade')

print('-='*20)
print('\033[31mTela para acessar o log in da microsoft\033[m')
print('=-'*20)

geral = list()
dadospess = list()
login = []
ad = list()
print('[1] Acessar conta', end=''
      '\n[2] Criar a conta')

while True:
    p = str(input('Qual das opções: '))
    if p in 1 and 2:
        print('Erro, digite uma opção valida')
    else:
        break

for c in range(0, 1):
    ad.append(str(input('digite o seu nome: ')))
    ad.append(int(input('Qual a sua idade: ')))
    geral.append(ad[:])
    ad.clear()

