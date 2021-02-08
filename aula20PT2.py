'''from time import sleep
def contador(i, f, p):
    """
    Faz uma contagem e mostra o resultado na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo(salto) da contagem
    :return: Sem retorno
    Função criada por Lucas Galves assistindo Curso em Vídeo - Aula  21
    """
    c = i
    while f >= c:
        print(f'{c} ', end='')
        c += p
    print('FIM')

help(contador)
#contador(2, 10, 2)'''



'''def somar(* valores):
    """
    Faz a soma de três valores e mostra o resultado na tela.
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    Criado por Lucas Pereira Galves
    """
    soma = 0
    for numero in valores:
        soma += numero
    print(f'O valor da soma é: {soma}')

somar(3, 2, 5)
somar(3, 2)
somar(3, 2, 5, 10)'''


'''def teste():
    x = 8
    print(f'Na função teste "x" vale: {x}')

teste()
print(x)'''



'''def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'Dentro da função "A" vale: {a}')
    print(f'Dentro da função "B" vale: {b}')
    print(f'Dentro da função "C" vale: {c}')

a = 5
teste(a)
print(f'Fora da função "A" vale: {a}'''


'''def somar(a=0, b=0, c=0):
    soma = a + b + c
    return soma

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os valores dos retornos são: {r1}, {r2}, {r3}')'''


#O fatorial precisa receber um parâmetro de um número,
# e se não receber, será o valor 1 e se tornou um
# parâmetro opcional(para não valer zero)
'''def fatorial(num=1):
    f = 1 #Local
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os retornos são: {f1}, {f2}, {f3}.')'''


def par(valor=0):
    if valor % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é ímpar.')



