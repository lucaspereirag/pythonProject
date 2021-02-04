lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

par = terceiraCol = segundaLinhaSoma = segundaLinhaMaior = 0

for posicao in range(0, 3):
    for elemento in range(0, 3):
        lista[posicao][elemento] = int(input(f'Número [{posicao}][{elemento}]: '))
        if lista[posicao][elemento] % 2 == 0:
            par += lista[posicao][elemento]

for posicao in range(0, 3):
    terceiraCol += lista[posicao][2]

for elemento in range(0, 3):
    segundaLinhaSoma += lista[1][elemento]
    if elemento == 0:
        segundaLinhaMaior = lista[1][elemento]
    elif lista[1][elemento] > segundaLinhaMaior:
        segundaLinhaMaior = lista[1][elemento]


for posicao in range(0, 3):
    for elemento in range(0, 3):
        print(f'[{lista[posicao][elemento]:^5}]', end='')
    print()

print(f'A soma dos pares: {par}')
print(f'A soma dos números na 3º Coluna: {terceiraCol}')
print(f'A soma da Segunda Linha: {segundaLinhaSoma}')
print(f'O maior valor da Segunda Linha: {segundaLinhaMaior  }')