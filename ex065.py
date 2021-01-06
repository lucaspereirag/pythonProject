continuar = 's'
contar = 0
qtdNumeros = qtd = somar = media = maior = menor = 0

while continuar != 'N':
    contador = int(input('\n\033[41mQuantos números deseja: \033[m '))
    while contador > contar:
        numero = int(input('Digite um número({}): '.format(qtd + 1)))
        contar += 1
        somar += numero
        qtd += 1
        if qtd == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    media = somar
    qtdNumeros += contador
    print('\nA média entre os valores: {:.2f}'
          '\nO maior valor lido: {}'
          '\nO menor valor lido: {}'.format(media / qtdNumeros, maior, menor))
    continuar = str(input('\033[7;30mDeseja continuar? [s/n]\033[m\n')).strip().upper()
    contar = 0

print('\033[42mObrigado por utilizar o programa!\033[m')
