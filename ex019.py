from random import choice
n1 = str(input('Primeiro Ministro: '))
n2 = str(input('Segundo Ministro: '))
n3 = str(input('Terceiro Ministro: '))
n4 = str(input('Quarto Ministro: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('A lista de Ministros é: {}'.format(lista))
print('O Ministro(a) escolhido foi: {}'.format(escolhido))


