
pessoas = []
dados = list()

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
dados.append(nome)
dados.append(idade)
pessoas.append(dados)
dados = []

print(pessoas)
with open('pessoas.txt','a') as arquivo:
    for valor in pessoas:
        arquivo.write(str(valor) + '\n')
with open('pessoas.txt','r') as arquivo:
    for k, v in pessoas:
        print(f"{k}^:             {v}")



