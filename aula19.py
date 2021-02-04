
estado = dict() #estados serão dicionários
brasil = list() #brasil será uma lista composta por estados

#desejo ler 3 estados:
for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    #essa leitura acima será realizada 3 vezes.
    #Ainda é preciso adicionar os estados a lista Brasil.
    brasil.append(estado.copy())
    #Fim da Alimentação

for est in brasil:
    for v in est.values():
        print(v, end=', ')
    print()
    #fim da impressão dos dados











'''
#Dicionário dentro de lista:

brasil = []#lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}#dicionario
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}#dicionario

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

'''print(f'Estado 1: {estado1}')
print(f'Estado 2: {estado2}')
print(f'Lista Brasil Inteira: {brasil}')
print(f'Brasil o dicionário 1: {brasil[0]}')
print(f'Brasil o dicionário 2: {brasil[1]}')'''






'''pessoas = {'nome': 'Lucas', 'idade': 26, 'sexo': 'M'}

#del pessoas['sexo']
pessoas['nome'] = 'Laura'
pessoas['peso'] = 45

for k, v in pessoas.items():
    print(f'O {k} = {v}')'''





#print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')

#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())