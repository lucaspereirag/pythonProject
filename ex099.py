from time import sleep
lista = []

def maior (* numeros):
    for i in numeros:
        lista.append(i)
    print('Analisando os dados...')
    sleep(1)
    print(f'Foram informados os valores: {lista}.')
    sleep(1)
    print(f'O tamanho da lista é de {len(lista)} números.')
    sleep(1)
    if len(lista) >= 1:
        print(f'O maior número na lista é o {max(lista)}.')
    else:
        print(f'Não há valores para comparação.')
    print('-' * 30)
    lista.clear()




maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
