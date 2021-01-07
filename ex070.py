print('-~-' * 10, '\nPet Shop Baracão',  '~._.~')
print('-~-' * 10)

cont = total = prod100 = prodCaro = prodBarato = maior = menor = 0

while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    if cont == 0:
        maior = menor = preco
        prodCaro = prodBarato = nome
    elif preco > maior:
        maior = preco
        prodCaro = nome
    else:
        menor = preco
        prodBarato = nome
    cont += 1
    total += preco
    if preco > 100:
        prod100 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'-~-' * 15,
      f'\nO valor Total Gasto na compra: R$ {total:.2f}'
      f'\n{prod100} produto(s) custa(m) mais de R$ 100,00'
      f'\nO produto mais caro foi {prodCaro}: R$ {maior:.2f}'
      f'\nO produto mais barato foi {prodBarato}: R$ {menor:.2f}')
