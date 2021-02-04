from datetime import date

pessoas = {}
listaDePessoas = []
hoje = date.today().year
somaIdade = mediaIdade = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Digite apenas "M" ou "F".')
    idade = int(input('Ano de Nascimento: '))
    pessoas['idade'] = hoje - idade
    somaIdade += pessoas['idade']
    listaDePessoas.append(pessoas.copy())
    while True:
        continuar = str(input('Deseja continuar?[S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite apenas "SIM" ou "NÃO".')
    if continuar in 'N':
        break
pessoas.clear()

print('-=' * 25)
print(listaDePessoas)

print('-=' * 12, 'Total de Pessoas Cadastradas ', '-=' * 12)
print(f'Total de pessoas cadastradas: {len(listaDePessoas)}')

print('-=' * 10, 'A média das Idades ', '-=' * 10)
mediaIdade = somaIdade / len(listaDePessoas)
print(f'A média das Idades: {mediaIdade} anos.')


print('-=' * 10, 'Lista com Todas as Mulheres', '-=' * 10)
for elemento in listaDePessoas:
    if elemento['sexo'] in 'F':
        print(f'{elemento["nome"]}')
print()

print('-=' * 10, 'Lista de Pessoas Acima da Média de Idade ', '-=' * 10)
for elemento in listaDePessoas:
    if elemento['idade'] >= mediaIdade:
        print(f'{elemento["nome"]} está acima da Média da Idade. ')
print()