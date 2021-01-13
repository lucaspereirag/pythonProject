lista = list()
continuar = ''

while True:
    num = (int(input('Digite um número: ')))
    if num in lista:
        print(f'\033[31mNúmero {num} já está na lista, não vou adicionar...\033[m')
    else:
        lista.append(num)
        print(f'\033[32mValor {num} adicionado com sucesso!\033[m')
    continuar = str(input('\033[30;47mDeseja continuar? [S/N]:\033[m ')).strip().upper()[0]
    if continuar == 'N':
        break

print('_x' * 15)
print(f'\033[7mOs valores da lista: {sorted(lista)}\033[m')
