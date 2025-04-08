num = []
for cont in range(0, 5):
    num.append(int(input('Digite um número: ')))
print(num)
print(f'o maior valor é {max(num)} e a sua posição é {num.index(max(num))}')
print(f'O menor valor é {min(num)} e a sua posição é {num.index(min(num))}')