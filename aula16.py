#3 tipos de inicialização de tuplas: (tupla) ou [lista] ou {dicionário}

"""lancheSimples = 'Hamburguér'
lancheSimples= 'Sucão'
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(f'O tamanho da tupla de lanche: {len(lanche)}\n')

for comida in range(0, len(lanche)):
    print(f'Hoje eu comi {lanche[comida]} que é a posição {comida}')
print('Terminei de comer tudo e engordei.')

print('-=' * 25)

# Não mostra o contador:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Terminei de comer tudo.')

#print(lancheSimples)
#print(lanche)
#print((lanche[1:3]))
#print(lanche[-1])
#print(lanche[-4])
#print(lanche[:2])
#Tuplas São Imutáveis:
#lanche[1] = 'Refrigerante'
#print(lanche[1])

print('-=' * 25)

print(sorted(lanche))"""

"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'Tupla A: {a})')
print(f'Tupla B: {b}')
print(f'Tupla C: {c}')
print(f'O tamanho da tupla somada: {len(c)}')
print(f'O número 5 aparece {c.count(5)} vezes')
print(f'O número 8 está no index da posição: {c.index(8)}')
print(f'O número 5 está no index da posição: {c.index(5, 2)}')"""


pessoa = ('Lucas', 26, 'M', 83.2)
del(pessoa)
print(pessoa)

