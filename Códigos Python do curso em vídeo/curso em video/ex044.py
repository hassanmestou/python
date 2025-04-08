# produto
print('{:=^40}'.format('lojas HASSAN'))
produto = float(input('Digite o preço do produto: '))
print('você pagara em que forma')
print('[ 1 ] Á Vista cheque de: 10% de desconto')
print('[ 2 ] Á VISTA no cartão: 5% de desconto')
print('[ 3 ] 2x no cartão: preço normal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
opcao = int(input('Qual opção de pagamento você vai querer: '))
if opcao == 1:
    total = produto - (produto * 10 / 100)
elif opcao == 2:
    total = (produto * 5 / 100)
elif opcao == 3:
    total = produto
    parcela = total / 2
    print('Sua compra escolhida será parcelada em 2x de {:.2f}'.format(parcela))
elif opcao == 4:
    total = produto + (produto * 20 / 100)
    tal = int(input('Em quantas parcelas: '))
    parcela = total / tal
    print('sua compra foi parcelada em {}x de {:.2f}R$ com juros'.format(tal, parcela))
else:
    total = produto
    print('\033[31mOPCÃO INVALIDA\033[m')
print('sua compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, total))




