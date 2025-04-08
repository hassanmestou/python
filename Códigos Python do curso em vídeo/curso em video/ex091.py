import random
from time import sleep
from operator import itemgetter
jog = {'jog1': random.randint(1, 6),
       'jog2': random.randint(1, 6),
       'jog3': random.randint(1, 6),
       'jog4': random.randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jog.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jog.items(), key=itemgetter(1) reverse=True)
print('Ranking+')
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')







