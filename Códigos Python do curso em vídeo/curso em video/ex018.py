import math
angulo = float(input('digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('\033[33mo ângulo de\033[m \033[36m{}\033[m \033[33mtem o SENO de\033[m \033[m{:.2f}\033[m'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('\033[31mo ângulo de\033[m \033[36m{} \033[31mtem como o cosseno\033[m {:.2f}'.format(angulo, cos))
tg = math.tan(math.radians(angulo))
print('\033[32mo angulo\033[m \033[36m{} \033[32mtem como tangente\033[m {:.2f}'.format(angulo, tg))


