preco = ('Lapís', 1.00,
         'Hambúrguer', 6.00,
         'Borracha', 3.00,
         'Lápis de cor', 20.00,
         'Parmesiana', 40.00)
print('-='*20)
print(f'{"Listagem de preços":^30}')
print('\033[31m-\033[m'*40)
for cont in range(0, len(preco)):
    if cont % 2 == 0:
        print(preco[cont],end='..................R$')
    elif cont % 2 == 1:
        print(preco[cont])
print('-'*40)














