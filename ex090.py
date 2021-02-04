
aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
situacao = ' '
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print(aluno)

print(f'O aluno {aluno["nome"]} teve a média {aluno["media"]} e está {aluno["situacao"]}')
print('-=' * 15)

for k,v in aluno.items():
    print(f'{k} é igual a {v}')

