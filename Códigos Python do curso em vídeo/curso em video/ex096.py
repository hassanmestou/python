print('controle de terrenos')
print('-='*20)
def area(largura, comprimento):
    s = largura * comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {s}m')

largura= float(input('Digite a largura: '))
comprimento = float(input('Qual o comprimento: '))
area(largura, comprimento)