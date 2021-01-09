from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
#com for
print('Os valores da Lista com For rodando: ', end='')
for c in tupla:
    print(f'{c} ', end='')

#Sem for:
print(f'\nA lista vale: {tupla}')
print(f'O maior elemento da lista: {max(tupla)}')
print(f'O menor elemento da lista: {min(tupla)}')

