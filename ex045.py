from random import randint
from time import sleep

lista = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)
if computador == 1:
    itemPC = 'Pedra'
elif computador == 2:
    itemPC = 'Papel'
else:
    itemPC = 'Tesoura'


jogador = int(input('Escolha o seu número: \n'
                    '[0] Pedra '
                    '[1] Papel '
                    '[2] Tesoura '
                    '\nSelecione: '))
if jogador == 1:
    itemJogador = 'Pedra'
elif jogador == 2:
    itemJogador = 'Papel'
else:
    itemJogador = 'Tesoura'


print('Jo-', end='')
sleep(0.7)
print('Ken-', end='')
sleep(0.7)
print('Pô!')

print('-=' * 14)
print('Computador escolheu: {}'
      '\nJogador escolheu: {}'.format(lista[computador], lista[jogador]))
print('-=' * 14)

if computador == 0:#Computador jogou Pedra:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador venceu! {} vence {}'.format( lista[jogador], lista[computador]))
    elif jogador == 2:
        print('Computador venceu! {} vence {}'.format(lista[computador],  lista[jogador]))
    else:
        print('Jogada Inválida!')
elif computador == 1:#Computador jogou Papel:
    if jogador == 0:
        print('Computador venceu! {} vence {}'.format(lista[computador],  lista[jogador]))
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu! {} vence {}'.format( lista[jogador], lista[computador]))
    else:
        print('Jogada Inválida!')
elif computador == 2:#Computador jogou Tesoura:
    if jogador == 0:
        print('Jogador venceu! {} vence {}'.format( lista[jogador], lista[computador]))
    elif jogador == 1:
        print('Computador venceu! {} vence {}'.format(lista[computador],  lista[jogador]))
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada Inválida!')

