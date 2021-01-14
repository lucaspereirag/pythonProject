listaprin = []
listapar = []
listaimpar = []

while True:
    listaprin.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('\033[7mDeseja continuar: [S/N]:\033[m ')).strip().upper()[0]
    if continuar == 'N':
            break
for valor in listaprin:
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)

listapar.sort()
listaimpar.sort()
print('x-' * 20)
print(f'\033[33mLista: {listaprin}\033[m')
print(f'\033[34mLista Par: {listapar}\033[m')
print(f'\033[35mLista Ímpar: {listaimpar}\033[m')
