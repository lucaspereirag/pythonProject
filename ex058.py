from random import randint

computador = randint(1, 10)
usuario = int(input('Digite um valor entre 1 a 10: '))
tentativas = 1

while usuario != computador:
    if usuario > 10:
        print('\033[41mEI! PARE DE ROUBAR! O LIMITE É ATÉ 10!\033[m'
              '\nTente novamente, computador escolheu: {}'.format(computador))
    else:
        print('Quase! Você pensou no número diferente do computador: {}'.format(computador))
    if usuario != computador:
      tentativas += 1
    computador = randint(1, 10)
    usuario = int(input('Digite um valor entre 1 a 10: '))

print('\033[1;30;42mParabéns!\033[m Você chutou o nº {} e adivinhou o nº {} do computador!'
      '\nTotal de tentativas: {}'.format(usuario, computador, tentativas))
