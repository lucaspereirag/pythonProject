from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2) #sorteio aleatório do número
print('Computador pode escolher: {}'.format(itens))
print('Escolha do computador númerica: {}'.format(computador)) #computador dá um número
print('Escolha do computador: {}'.format(itens[computador])) #item na posição computador


print('''Suas Opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual a sua jogada: '))
print('-=' * 15)
print('Computador escolheu: {}'.format(itens[computador]))
print('Jogador escolheu: {}'.format(itens[jogador]))
print('-=' * 15)
