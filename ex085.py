num = [[], []]

for c in range (0, 7):
    valor = int(input(f'Número {c + 1}: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Os números pares: {num[0]}')
print(f'Os números ímpares: {num[1]}')
