nome = str(input("Digite o seu nome: "))
meu = open('teste.txt', 'a')
meu.write(f'\n{nome}')
meu.close()
idade = int(input("Digite a sua idade: "))
meu = open('teste.txt', 'a')
meu.write(f'{idade}\n')
meu.close()


meu = open('teste.txt', 'r')
pessoas = meu
for c in pessoas:
    print(f'{c}')




