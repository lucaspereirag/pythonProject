'''
Faça um programa que tenha uma função chamada “escreva()”,
que recebe um texto qualquer como parâmetro e mostre uma mensagem com tamanho variável.
'''

def escreva(palavra):
    print('~' * n)
    print(f'  {palavra}')
    print('~' * n)

palavra = str(input('Digite algo: '))
n = len(palavra) + 4

escreva(palavra)