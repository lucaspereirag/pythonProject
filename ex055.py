
maior = 0
menor = float('inf')

for c in range (0, 5):
    peso = float(input('Digite peso da {}º pessoa: '.format(c + 1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi o: {} kg'.format(maior))
print('O menor peso foi o: {} kg'.format(menor))

