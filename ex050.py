
soma = 0
cont = 0
for numero in range(0, 6):
    pares = int(input('Digite o {}º número: '.format(numero + 1)))
    if pares % 2 == 0:
        cont += 1
        soma += pares
print('O total de números pares é: {}'
      '\nA soma dos números pares é: {}'.format(cont, soma))
print('FIM')

