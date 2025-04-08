d = float(input('diga a altura da sua parede: '))
od = float(input('diga a largura da parede: '))
c = d * od
cf = c/2
print('a aréa de sua parede será, de \033[0;31m{:.3f}\033[m \n e você precisará de \033[4;36m{}L\033[m de tinta para pintar \033[0;31m{}m quadrados'.format(c, cf, c))
