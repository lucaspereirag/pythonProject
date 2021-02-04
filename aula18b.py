galera = list()
dados = []
maiorIdade = menorIdade = 0

for contador in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

'''print('-=' * 30)

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''

print('-=' * 30)

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade. Possui idade de {pessoa[1]} anos de idade.')
        maiorIdade += 1
    else:
        print(f'{pessoa[0]} é menor de idade. Possui idade de {pessoa[1]} anos de idade.')
        menorIdade += 1

print('-=' * 30)
print(f'Quantidade de maiores de idade: {maiorIdade}')
print(f'Quantidade de menores de idade: {menorIdade}')