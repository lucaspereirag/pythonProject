palavras = ('Laura', 'Lucas', 'Tony', 'Nina', 'Casa', 'Apartamento', 'Trabalho',
         'Estagio', 'Faculdade', 'Europa')


for p in palavras:
    print(f'\nA palavra {p} tem vogais: ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}', end='')
