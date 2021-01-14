lista = []

while True:
    lista.append(int(input('\033[1mDigite um valor:\033[m ')))
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('\033[30;47mDeseja continuar? [S/N]:\033[m ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 30)
print(f'A lista: {lista}')
print('-=' * 30)
lista.sort(reverse=True)
print(f'\033[7mA lista Reversa: {lista}\033[m')
print('-=' * 30)
lista.sort(reverse=False)
print(f'A lista em ordem crescente: {lista}')
print('-=' * 30)
print(f'O tamanho da lista: {len(lista)}')
print('-=' * 30)
if 5 in lista:
    print(f'\033[32mO valor 5 está na lista.\033[m')
else:
    print(f'\033[31mO valor 5 não está nessa lista.\033[m')