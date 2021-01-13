
tupla = (int(input('Digite o número 1: ')), int(input('Digite o número 2: ')),
          int(input('Digite o número 3: ')),int(input('Digite o número 4: ')),
          int(input('Digite o número 5: ')))

print(f'Tupla: {tupla}')
print(f'O número 9 apareceu: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu pela primeira vez na posição {tupla.index(3) + 1}')
'''else:
    print('O número 3 não estava na lista!')'''

par = impar = 0
for elemento in tupla:
    if elemento % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'O total de pares: {par}')
print(f'O total de ímpares: {impar}')
