lista = ['-----1 pessoa----', '-----2 pessoas-----', '-----3 pessoa----', '---=-=-=-=4 pessoa--=-=-=-=-']
soma = 0
sf = 0
maior = 0
menor = 0
p = 0
m = 0
quantidade = 0
for lista in lista:
    print(lista)
    soma += 1
    for c in range(1, 2):
        nome = str(input('Digite seu nome: '))
        idade = int(input('Qual a sua idade: '))
        s = str(input('Qual o seu sexo:[M/F] '))
        sf += idade / 4
        if lista == 1 and s in 'Mm':
            maior = idade
            nome = nome
        else:
            if s in 'Mm' and idade > maior:
                maior = idade
                p = nome
        if s == 'f' or s == 'F' and idade <= 20:
            m += 1
print('A medía das idades e de {:.1f} anos, das pessoas acima'.format(sf))
print('O homem mais velho tem {} anos e ele é {}'.format(maior, p))
print('A quantidade de mulheres que tem menos de 20 anos é {}'.format(m))
