lista = list()
pessoas = []
maisPesado = maisLeve = 0

while True:
    lista.append(str(input('Nome: ')).strip())
    lista.append(int(input('Peso: ')))
    if len(pessoas) == 0:#realizar o maior e menor antes de limpar a lista.
        maisPesado = maisLeve = lista[1]
    else:
        if lista[1] > maisPesado:
            maisPesado = lista[1]
        elif lista[1] < maisLeve:
            maisLeve = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print(pessoas)
print(f'A quantidade de cadastradas foi: {len(pessoas)}')
print(f'O maior peso: {maisPesado} kgs, as pessoas: ', end='')
for p in pessoas:
    if p[1] == maisPesado:
        print(f'"{p[0]}" ', end='')
print(f'\nO mais leve: {maisLeve} kgs, as pessoas: ', end='')
for p in pessoas:
    if p[1] == maisLeve:
        print(f'"{p[0]}"', end='')



