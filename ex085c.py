lista = [[], []]

for cont in range(0, 4):
    numero = int(input(f'Número {cont + 1}: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print(f'Números pares: {lista[0]}')
print(f'Números ímpares: {lista[1]}')