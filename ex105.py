
def notas():
    dictNotas = {}
    listaNotas = []
    from statistics import mean
    qtdNotas = int(input('Quantas notas: '))
    for c in range(qtdNotas, 0, -1):
        notas = float(input('Digite uma nota: '))
        listaNotas.append(notas)
    dictNotas['notas'] = listaNotas[:]
    dictNotas['total'] = len(listaNotas)
    dictNotas['maior'] = max(listaNotas)
    dictNotas['menor'] = min(listaNotas)
    dictNotas['media'] = mean(listaNotas)
    if dictNotas['media'] < 6:
        situacao = 'Má situação'
    elif dictNotas['media'] <= 8:
        situacao = 'Situação Ok'
    else:
        situacao = 'Aluno está muito bem!'
    dictNotas['situacao'] = situacao
    listaNotas.clear()
    return dictNotas
nome = str(input('Digite o nome do aluno: '))
notaNome = notas()
print(f'Os valores de {nome}: \n{notaNome}')