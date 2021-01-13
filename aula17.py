"""num = (2, 5, 9, 1)
print(num)
print(num[0])
num[0] = 1"""

'''num = [2, 5, 9, 1]
print(num)
print(num[0])
num[0] = 500
print(num)'''

"""num = [2, 5, 9, 1]
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)#insira o num 2 na posição 2
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4.')
print(num)

print(f'A minha lista tem {len(num)} elementos.')"""


'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}...')
print('Final da Lista')'''


'''valores = list()

for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}...')
print('Final da Lista')'''


a = [2, 3, 4, 7]
b = a[:] #O [:] vai criar uma cópia dos seus valores, não ligação
b[2] = 8 #espera-se que somente B recebe 8, como assim foi copiado, somente B altera.
print(f'A lista A vale: {a}')
print(f'A lista B vale: {b}')

