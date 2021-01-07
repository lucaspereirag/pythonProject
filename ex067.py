print('-' * 30)
print('GERADOR DE TABUADA COM WHILE')
print('-' * 30, '\n')

cont = 0

while True:
    tabuada = int(input('Digite um número: '))
    if tabuada < 0:
        break
    while cont <= 10:
        print(f'{tabuada} x {cont} = {tabuada * cont}')
        cont += 1
    cont = 0
    print('-' * 30)

print('Obrigado por utilizar o Gerador de Tabuadas. '
      '\n\033[42mVolte Sempre!\033[m')
