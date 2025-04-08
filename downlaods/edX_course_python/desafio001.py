def receber(texto):
    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for letras in texto:
        x = 0
        for l in lista:
            if (x < 27):
                x += 1
            if (x > 26):
                break
            elif (x <= 26 and letras == l):
                print(f"{x}", end="")
                x = 0

string = input("Digite uma palavra: ")
receber(string)