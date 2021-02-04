'''
Faça um programa que tenha uma função chamada “área()”, que
receba as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.
'''

def area(largura, comprimento):
    totalArea = largura * comprimento
    print(f'O valor da área do terreno {largura:.2f}m² e '
          f'{comprimento:.2f}m² é de {totalArea:.2f}m²')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)