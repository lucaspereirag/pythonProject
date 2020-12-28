cidade = str(input('Digite o nome da cidade: ')).strip()
print('Analisando o nome da cidade {} ...'.format(cidade))
print(cidade[: 5].upper() == 'SANTO')
#Com "in":
analise = 'SANTO' in cidade[: 5].upper()
print(analise)
