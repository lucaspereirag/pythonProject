numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
parar = 's'
somar = subtrair = multiplicar = dividir = maior = menor = 0
from time import sleep

while parar != 'N':
    menu = int(input('Selecione um item abaixo:'
                     '\n[ 1 ] Somar'
                     '\n[ 2 ] Subtrair'
                     '\n[ 3 ] Multiplicar'
                     '\n[ 4 ] Dividir'
                     '\n[ 5 ] Maior e Menor'
                     '\n[ 6 ] Digitar novos números'
                     '\n[ 7 ] Sair do Programa'
                     '\nSelecionar: '))
    if menu == 1:
        somar = numero1 + numero2
        print('Os dois números somados: {}'.format(somar))
    elif menu == 2:
        subtrair = numero1 - numero2
        print('A subtração dos dois números: {}'.format(subtrair))
    elif menu == 3:
        multiplicar = numero1 * numero2
        print('A multiplicação dos dois números: {}'.format(multiplicar))
    elif menu == 4:
        dividir = numero1 / numero2
        print('A divisão do {} pelo {} é: {}'.format(numero1, numero2, dividir))
    elif menu == 5:
        if numero1 > numero2:
            print('O número 1 ({}) é maior que o número 2 ({})'.format(numero1, numero2))
        else:
            print('O número 2 ({}) é maior que o número 1 ({})'.format(numero2, numero1))
    elif menu == 6:
        numero1 = float(input('Digite um número: '))
        numero2 = float(input('Digite outro número: '))
    elif menu == 7:
        parar = 'N'
    else:
        print('Opção Inválida.')
    sleep(1)
print('FIM')