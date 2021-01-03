tot = 0
num = int(input('Digite um número: '))

for contador in range(1, num + 1):
    if num % contador == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(contador), end=' ')
print('\n\033[mO número {} foi dividido {} vezes.'.format(num, tot))
if tot == 2:
    print('Número primo.')
else:
    print('Não é primo')
