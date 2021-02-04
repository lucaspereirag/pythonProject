jogador = {}
jogadores = []
listaGols = []

#INÍCIO DA LEITURA DOS DADOS DOS JOGADORES
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Partidas do {jogador["nome"]}: '))
    for cont in range(0, jogador['partidas']):
        gols = int(input(f'Gols na {cont + 1}º partida: '))
        listaGols.append(gols)
        jogador['gols'] = listaGols[:]
        jogador['saldoGol'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    listaGols.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite apenas "Sim" ou "Não".')
    if continuar in 'N':
        break
#FIM DA LEITURA DOS DADOS


#INÍCIO DAS IMPRESSÕES DA LISTA DOS JOGADORES
print('-=' * 15, 'Estatisticas do Jogador ', '-=' * 15)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for chave, valor in enumerate(jogadores):
    print(f'{chave:>4} ', end='')
    for dados in valor.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-' * 60)
#FIM DA IMPRESSÃO DA LISTA DOS JOGADORES



#INÍCIO DA BUSCA DOS JOGADORES:
while True:
    busca = int(input('Digite o jogador que deseja obter dados [999 Finaliza o programa]: '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Erro! Não existe jogador com código {busca}.')
    else:
        print(f' -- Estatisticas do jogador {jogadores[busca]["nome"]} -- ')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'      No jogo {i + 1} fez {g} gols.')
    print('-' * 60)