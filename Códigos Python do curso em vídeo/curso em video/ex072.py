numeros = ('zero', 'Um', 'Dois', 'três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito','Nove', 'Dez',
           'onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',
           'Vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num >= 21:
        print('Tente Novamente',end=' ')
    else:
        break
print(numeros[num])






