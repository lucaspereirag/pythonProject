matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = somaColuna = 0

# FOR de alimentação da matriz
for linha in range(0, 3):#de 0 a 3 porque tem 0 1 e 2, o 3ignora.
    for coluna in range(0, 3): #mesma lógica acima
        matriz[linha][coluna] = int(input(f'Número para [{linha}][{coluna}]:'))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]




print('-='  * 25)
#for de impressão da matriz:
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz [linha][coluna]:^5}]', end='')#5 casas decimais e centralizado (^)
    print()#quebra a cada coluna que ele lê


print('-='  * 25)
print(f'A soma dos Pares: {par}')
print('-='  * 25)
for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print(f'A soma dos valores da 3º coluna: {somaColuna}')

print('-='  * 25)
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maior}')
print('-='  * 25)
