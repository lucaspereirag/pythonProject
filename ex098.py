'''
Faça um programa que tenha uma função chamada “contador()” que
receba três parâmetros: Início, Fim e Passo. Realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
(Sem desempacotamento) – ( Tem que funcionar com passo negativo também, ex: - 2)
– (Se passo = 0, assumir passo = 1 ou -1).
A.	De 1 até 10, de 1 em 1
B.	De 10 até 0, de 2 em 2
C.	Uma contagem personalizada
'''
from time import sleep
def mostraLinha():
    print('-' * 30)

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} a {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1 #converte de negativo pra positivo
    if passo == 0:
        passo = 1
    if fim > inicio:
        cont = inicio
        while fim >= cont:
            print(f'{cont} ', end='')
            #sleep(0.4)
            cont += passo
        print('Fim')
    if inicio > fim:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            #sleep(0.4)
            cont -= passo
        print('Fim')



inicio = 1
fim = 10
passo = 1
contador(inicio, fim, passo)

mostraLinha()
inicio = 10
fim = 0
passo = 2
contador(inicio, fim, passo)

mostraLinha()
# Programa Principal:
print('Contagem Personalizada')
mostraLinha()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
