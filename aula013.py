soma = 0
for c in range (0, 3):
    numero = int(input('Digite o número {}: '.format(c + 1)))
    soma += numero
print('A soma dos {} números é: {}'.format(c + 1, soma))
print('FIM')