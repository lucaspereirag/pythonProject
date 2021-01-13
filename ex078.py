lista = list()
cont = 0

for contador in range(0, 5):
    lista.append(int(input(f'Digite o número {contador + 1}: ')))

'''while cont < 5:
    lista.append((int(input(f'Digite o número {cont + 1}: '))))
    cont += 1'''
maior = max(lista)
menor = min(lista)

print(f'A lista: {lista}')

print(f'O maior valor da lista: {maior} nas posições: ', end='')
for posicao, valores in enumerate(lista):
    if valores == maior:
        print(f'{posicao}...', end='')

print(f'\nO menor valor da lista: {min(lista)}, nas posições: ', end='')
for posicao, valores in enumerate(lista):
    if valores == menor:
        print(f'{posicao}...', end='')



