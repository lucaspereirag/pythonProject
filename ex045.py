from random import randint
from time import sleep

numero1 = randint(1, 3)
if numero1 == 1:
    computador = 'Pedra'
elif numero1 == 2:
    computador = 'Papel'
else:
    computador = 'Tesoura'


numero2 = int(input('Escolha o seu número: \n'
                    '[1] Pedra '
                    '[2] Papel '
                    '[3] Tesoura '
                    '\nSelecione: '))
if numero2 == 1:
    jogador = 'Pedra'
elif numero2 == 2:
    jogador = 'Papel'
else:
    jogador = 'Tesoura'


print('Computador: {}'
      '\nJogador: {}'.format(computador, jogador))

print('Jo-', end='')
sleep(0.7)
print('Ken-', end='')
sleep(0.7)
print('Pô!')
if numero1 > numero2:
    print('Computador venceu, pois {} vence {}.'.format(computador, jogador))
elif numero1 == numero2:
    print('Empate!')
else:
    print('Jogador venceu, pois {} vence {}.'.format(jogador, computador))
