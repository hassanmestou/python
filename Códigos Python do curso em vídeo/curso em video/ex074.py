from random import randint
num = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20),
       randint(1, 20))
print('\033[35mOs valores sorteados foram\033[m: ')
print(num)
print('\033[31m=-\033[m'*20)
print(f'O maior valor sorteado foi: {max(num)}')
print(f'O menor valor sorteado foi: {min(num)}')





