

tupla = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
    'nove','dez', 'onze', 'doze', 'treze','quatorze','quinze','dezesseis','dezessete'
         ,'dezoito','dezenove','vinte')
sair = ' '
while sair != 'S':
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente.')
    print(f'Você digitou o número {tupla[numero]}')
    sair = ' '
    while sair not in 'SsNn':
        sair = str(input('Deseja sair [S/N]: ')).upper().strip()[0]


