"""Programa que comparar dois números inteiros e retorna infos de igualdade"""

n1 = int(input('Digite o Primeiro Número Inteiro: '))
n2 = int(input('Digite o Segundo Número Inteiro: '))


if n1 > n2:
    print('O nº {} é maior que o nº {}.'.format(n1, n2))
elif n1 < n2:
    print('O nº {} é maior que o nº {}.'.format(n2, n1))
else:
    print('O nº {} é igual ao nº {}.'.format(n1, n2))