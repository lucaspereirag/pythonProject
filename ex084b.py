lista = list()
dados = []
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    if len(lista) == 1:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    dados.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 20)
print(lista)
print('-=' * 20)
print(f'A quantidade de pessoas cadastradas: {len(lista)}')
print('-=' * 20)
print('Pessoas mais pesadas: ',end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} ', end='')

print('\nPessoas mais leves: ',end='')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'{pessoa[0]} ', end='')
