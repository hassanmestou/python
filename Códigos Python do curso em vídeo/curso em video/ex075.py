núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite uo ultimo número: ')))
print('Os valores digitados foram: ')
print(núm)
print(f'Tem {núm.count(9)} noves nos valores acima')
if 3 in (núm):
       print(f'O Três está na posição {núm.index(3)+1}ª')
else:
       print('O três não tem posição')
print('Os valores pares são: ')
for num in núm:
       if num % 2 == 0:
              print(num, end=' ')




