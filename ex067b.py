print('-' * 30)
print('GERADOR DE TABUADA COM FOR')
print('-' * 30, '\n')

while True:
    tabuada = int(input('Digite um número: '))
    if tabuada < 0:
        break
    for c in range (0, 10):
        print(f'{tabuada} * {c} = {tabuada * c}')
    print('-' * 20)

print('Obrigado por utilizar o Gerador de Tabuadas. '
      '\n\033[42mVolte Sempre!\033[m')