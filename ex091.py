from random import randint
from time import sleep
from operator import itemgetter

jogador = {'jogador 1': randint(1, 6),
           'jogador 2': randint(1, 6),
           'jogador 3': randint(1, 6),
           'jogador 4': randint(1, 6)
           }
#dicionário ranking para criar ordem em jogadores:
ranking = {} #poderia ser uma lista ranking = []

print('A lista: ')
print(jogador)#somente mostra a lista
print('-='* 20)

#percorre/varre o dicionário e imprime:
print('Valores sorteados: ')
#para cada "chave" tirou o número "valor Da Chave"
for k, v in jogador.items():
    print(f'O {k} tirou o número:  {v}')
    sleep(1)

print('-='* 20)
#ordena o dicionário e ranking recebe o dicionário em forma de lista
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('-='* 25)
#percorre a lista ranking, o enumerate serve para o índice
#o valor serve para encontrar os valores de cada posição na lista do ranking
for indice, valor in enumerate(ranking):
    print(f'O {indice + 1}º lugar foi para: {valor[0]} que tirou {valor[1]} nos dados')