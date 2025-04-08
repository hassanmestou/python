print('-'*20)
print('sequencia de fibo')
print('-'*20)
n = int(input('Digite a quantidade de termos: '))
t1 = 0
t2 = 1
print('{} --> {}'.format(t1, t2), end=' --> ')
co = 3
while co <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' --> ')
    t1 = t2
    t2 = t3
    co += 1
print('fim', end='')
