produtos = ('Lápís', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)


for prod in range(0, len(produtos)):
    if prod % 2 == 0:
        print(f'{produtos[prod]:.<30}', end='')
    else:
        print(f'R$ {produtos[prod]:.2f}')


