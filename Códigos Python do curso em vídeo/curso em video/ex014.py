t = float(input('qual é a temperatura em celcius:C? '))
f = (t*1.8)+32
print('\033[36ma temperatura foi convertida. E em farenheit é\033[m \033[4;31m{:.1f}F'.format(f))
