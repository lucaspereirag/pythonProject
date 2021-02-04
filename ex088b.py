from random import randint
from time import sleep

lista = []
count = 0

sorteios = int(input('Digite quantos jogos gerados: '))

for qtdJogos in range(0, sorteios):
    for jogo in range(0, 6):
        while count < 6:
            numero = randint(1, 60)
            if numero not in lista:
                lista.append(numero)
                count += 1
    lista.sort()
    #sleep(1)
    print(f'Jogo nº {qtdJogos + 1}: [{lista}]')
    lista.clear()
    count = 0

print('-=' * 30)
print(f'<<<<< BOA SORTE! >>>>>>')