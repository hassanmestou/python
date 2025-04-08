n = int(input('\033[35mDigite o numero\033[m: '))
print('\033[35m-=-\033[m'*20)
print('Escolha abaixo o numero que você deseja transformalo')
print('\033[31m[\033[m \033[4;36m1\033[m \033[31m]\033[m binario:')
print('\033[32m[\033[m \033[4;35m2\033[m \033[32m]\033[m octadecimal:')
print('\033[33m[\033[m \033[4;34m3\033[m \033[37m]\033[m hexadecimal:')
print('\033[33m-=-\033[m'*20)
v = int(input('Escolha o número: '))
if v == 1:
    print('\033[36mO seu valor em numero binario é\033[m {}'.format(bin(n)[2:]))
elif v == 2:
    print('Seu numero em octal é {}'.format(oct(n)[2:]))
elif v == 3:
    print('O valor em numero hexadecimal é {}'.format(hex(n)[2:]))
else:
    print('OPs, deu um erro tente novamente')
