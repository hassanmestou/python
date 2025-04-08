preco = float(input('diga o preço normal do produto:R$ '))
promocao = int(input('diga o desconto: '))
m = promocao*preco
rf = m/100
pf = preco-rf
print('='*20)
print('sendo a promoção de \033[0;35m{}%\033[m o valor do produto será de \033[4;36m{}R$\033[m'.format(promocao, pf))



