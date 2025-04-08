def armazenarArquivo(nome):
    soma = 0
    soma += 1
    nom = open('pessoas.txt', 'a')
    valor = nome
    nom.write(f'{valor}')
    nom.close()

def exitir(nome):
    try:
        nom = open(nome, 'r')
    except FileNotFoundError:
        nom = open(nome, 'a')
        print("Arquivo criado com sucesso")

def lerArquivo(nome):
    nome = open(nome, 'r')
    nome = nome.readlines()
    for banda in nome:
        banda = banda.rstrip('\n')
        print(f'{banda}')

lerArquivo('pessoas.txt')
meu = open('pessoas.txt', 'r')
nome = [meu.readline()]
print(nome)

