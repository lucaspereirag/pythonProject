from random import randint

num = cont = 0
perdeu = False
parOuImpar = ' '
while True:
    numUsuario = int(input('Digite um número: '))
    numComputador = randint(0, 10)
    while parOuImpar not in 'PpIi':
        parOuImpar = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
    soma = numUsuario + numComputador
    if parOuImpar == 'P' and soma % 2 == 0:
        print('Jogador Venceu!')
        escolha = 'par'
    elif parOuImpar == 'I' and soma % 2 == 1:
        print('Jogador Venceu!')
        escolha = 'impar'
    else:
        print('GAME OVER! HA-HA-HA - Computador Venceu!')
        perdeu = True
        print(f'Total de Vitórias Consecutivas do Jogador: {cont}')
        if soma % 2 == 0:
            escolha = 'par'
        else:
            escolha = 'ímpar'
    if perdeu == True:
        break
    cont += 1
    parOuImpar = ' '
    print('-' * 40)

print(f'\nO computador escolheu {numComputador}.'
      f'\nO jogador digitou {numUsuario}. '
      f'\nE a soma {soma} é {escolha}')
print('-' * 40)

if cont >= 2:
    print(f'\033[32mIncrível! Você venceu {cont} vezes\033[m')
elif cont >= 1:
    print(f'\033[34mUau, você venceu {cont} vezes\033[m')
else:
    print('\033[31mVocê é uma vergonha.\033[m')



