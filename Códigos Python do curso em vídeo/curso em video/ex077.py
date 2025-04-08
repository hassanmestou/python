pala = ('Arroz', 'Feijao', 'Macarrao', 'Python', 'Programar', 'Viajar', 'Video-game')
for lista in pala:
    print(f'\nAs vogais da palavra {lista}', end=' ')
    for c in lista:
        if c.lower() in 'aeiou':
            print(c,end=', ')










