num = []
while True:
    nm = int(input('Digite um número: '))
    num.append(nm)
    r = str(input('Quer continuar [S/N]: '))
    if r in 'nN':
        break
print(num)
print(f'Foram digitados {len(num)} números')
num.sort(reverse=True)
print(f'Os valores em ordem decresente {num}')
if 5 in num:
    print('O 5 está nos números')
else:
    print('Ops... 5 não está presente')

