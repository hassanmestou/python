def alfabeto(num):
    alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    for n in range(num):
        print(f"{alfa[n]}", end=" ")
    




name = int(input("Digite um número de 1 a 26: "))
alfabeto(name)
