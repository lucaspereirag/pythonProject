from datetime import date

pessoas = {}
listaPessoas = []
hoje = date.today().year
somaIdade = mediaIdade = 0

while True:
    pessoas.clear() #pode usar clear em dicionário.
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoas['sexo'] not in 'MmFf':
            print('ERRO! Digite apenas "M" ou "F".')
        else:
            break
    idade = int(input('Ano de Nascimento [aaaa]:  '))
    pessoas['idade'] = hoje - idade
    somaIdade += pessoas['idade']
    listaPessoas.append(pessoas.copy())
    while True:
        continuar = str(input('Deseja continuar cadastrando pessoas? [S/N]: ')).strip().upper()
        if continuar in 'SN':
            break
        print('Erro! Digite apenas "S" ou "N".')
    if continuar == 'N':
        break
pessoas.clear()

print(listaPessoas)

print('-=' * 20)
# Retorna a qtd de Pessoas Cadastradas:
print(f'Quantidade de Pessoas Cadastradas: {len(listaPessoas)}.')

print('-=' * 20)
#Retorna a Média das Idades das pessoas:
mediaIdade = somaIdade / len(listaPessoas) # calcula a media da idade
print(f'Média das Idades: {mediaIdade:5.2f} anos.')#mediaIdade: 5 casas ao todos sendo 2 decimais.

print('-=' * 20)
#Varrer a lista de pessoas procurando por mulheres:
print('As mulheres cadastradas: ', end='')
for individuo in listaPessoas:
    if individuo['sexo'] in 'Ff':
        print(f'{individuo["nome"]}', end='')
print()

print('-=' * 20)
#Varrer a lista de pessoas com idade acima da média:
print('As pessoas com Idade acima da média: ')
for individuo in listaPessoas:
    if individuo['idade'] >= mediaIdade:
        print(f'O(a) {individuo["nome"]} tem idade acima da média '
              f'com idade de: {individuo["idade"]} anos.')
print()