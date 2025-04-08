#meu = open('teste.txt', 'r')
#print(meu.read())
#            ==
#meu = open('teste.txt')
#print(meu.read())

#Função write 'w'
#meu = open('teste.txt', 'w')
#meu.write('curso python')
#meu.close()
# a função 'w' sobrescreve um arquivo, ou sejá vai substituir a antiga frase

meu = open('teste.txt', 'a')
meu.write('\nola ')
meu.close()



