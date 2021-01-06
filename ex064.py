from time import sleep

numero = soma = count = 0
while numero != 999:
    numero = int(input('Digite um número: [999 Encerra o programa]: '))
    if numero != 999:
        soma += numero
        count += 1
    else:
        print('Encerrando o programa...')
        sleep(1)

print('A soma entre os números: {}'
      '\nA quantidade de números: {}'.format(soma, count))