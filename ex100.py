from random import randint

numeros = []

def sorteia():
    count = 0
    while count < 5:
        sorteio = randint(1, 10)
        if sorteio not in numeros:
            numeros.append(sorteio)
            count += 1
        numeros.sort()
    print(numeros)


def somarPar():
    somapar = 0
    for valor in numeros:
        if valor % 2 == 0:
            somapar += valor
    print(f'O valor dos pares: {somapar}')
    numeros.clear()


def somarParParametro(numeros):
    somaParParametro = 0
    for valor in numeros:
        if valor % 2 == 0:
            somaParParametro += valor
    print(f'A soma dos Pares com Função Recebendo Parâmetro é: {somaParParametro}')
    numeros.clear()


def mostraLinha():
    print('-=' * 30)




sorteia()
somarPar()
somarParParametro(numeros)
mostraLinha()
sorteia()
somarPar()
somarParParametro(numeros)
mostraLinha()
sorteia()
#somarPar()
somarParParametro(numeros)
mostraLinha()
sorteia()
#somarPar()
somarParParametro(numeros)