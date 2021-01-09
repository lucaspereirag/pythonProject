times = ('São Paulo', 'Internacional', 'Atletico-MG', 'Flamegno', 'Gremio', 'Palmeiras',
         'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR', 'Ceara', 'Atletico-GO',
         'Bragantino', 'Sport', 'Fortaleza', 'Vasco', 'Bahia', 'Goias', 'Botafogo', 'Coritiba')


print(f'Os 5 primeiros times no momento: {times[:5]}')
print('-x' * 40)
print(f'Os últimos 4 colocados no momento: {times[-4:]}')
print('-x' * 40)
print(f'A lista em ordem alfabética: {sorted(times)}')
print('-x' * 40)
print(f'A posição que o São Paulo está: {times.index("São Paulo") + 1}º')