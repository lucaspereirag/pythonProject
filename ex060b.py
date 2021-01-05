#Resolvendo o 060 com Módulo

#Módulo para calcular o fatorial:
from math import factorial

n = int(input('Digite um número para cálculo do fatorial: '))
fatorial = factorial(n)
print('O fatorial do número {}! é: {}'.format(n, fatorial))