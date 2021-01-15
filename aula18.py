'''lista = list()

lista.append('Lucas')
lista.append(26)
galera = []
galera.append(lista[:])
lista[0] = 'Laura'
lista[1] = 24
galera.append(lista[:])

print(galera)'''


'''galera = [['Laura', 24],['Lucas', 26],['Tony',3], ['Nina', 10]]

for pessoas in galera:
    print(f'{pessoas[0]} tem {pessoas[1]} anos de idade.')'''

'''for pessoa in galera:
    print(pessoa)#print de todos

print('-=' * 20)

for pessoa in galera:
    print(pessoa[0])#print só os nomes
'''
'''print(galera)
print(galera[0])
print(galera[0][0])
'''



#Criando Lista com Input do Usuário:
galera = []
dado = list()
maiorIdade = menorIdade = 0

for c in range(0, 3):
    dado.append(str(input('Digite Nome: ')))
    dado.append(int(input('Digite Idade: ')))
    galera.append(dado[:]) #cria uma cópia sem vínculo com dado
    dado.clear() #limpa a lista de dados para não armazenar dados desnecessários.

for pessoas in galera:
    if pessoas[1] >= 21:
        print(f'{pessoas[0]}, é maior de idade')
        maiorIdade += 1
    else:
        print(f'{pessoas[0]},não é maior de idade')
        menorIdade += 1

print(f'O nº de maiores: {maiorIdade}'
      f'\nO nº de menores: {menorIdade}')
