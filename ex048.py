
soma = 0
cont = 0
for multiplos in range(1, 501, 2):
    if multiplos % 3 == 0:
        cont += 1
        soma += multiplos
print('Valor da soma dos {} números: {}'.format(cont, soma))
print('end')
