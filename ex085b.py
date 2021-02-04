lista = []

for cont in range(0, 4):
    lista.append(int(input(f'Número {cont + 1}: ')))


lista.sort()

print(f'Lista com os pares: ',end='')
for numero in lista:
    if numero % 2 == 0:
        print(f'{numero} ', end='')

print(f'\nLista com os ímpares: ',end='')
for numero in lista:
    if numero % 2 == 1:
        print(f'{numero} ', end='')

