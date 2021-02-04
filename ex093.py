jogador = dict()
listaDeGols = list()
somaGols = 0

jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input((f'Quantidade de partidas do {jogador["nome"]}: ')))

for cont in range(0, jogador['partidas']): #Laço para contar partidas
   golsPartida = int(input(f'Gol da {cont + 1}º partida: ')) #Input de Gols por partida
   listaDeGols.append(golsPartida) #Lista que armazena cada gol x partida
   somaGols += golsPartida #total de gols

jogador['gols'] = listaDeGols[:] #dicionário que armazena a lista de gols.
jogador['totalGols'] = somaGols

print('-=' * 10, 'Dicionário do Jogador ', '-=' * 10)
print(jogador)

print('-=' * 11, 'Campos do Jogador ', '-=' * 11)
for k, v in jogador.items():
   print(f'O campo {k} tem valor {v}')

print('-=' * 10, 'Estatisticas do Jogador ', '-=' * 10)
print(f'O jogador {jogador["nome"]}, jogou {jogador["partidas"]} partidas.')
for indice, valor in enumerate(jogador["gols"]):
   print(f'  => Na partida {indice + 1}, o {jogador["nome"]} marcou {valor} gols.')