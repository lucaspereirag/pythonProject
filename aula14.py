"""for c in range(1, 10):
    print(c)
print('FIM')"""

#Bloqueando um Loop Infinito
"""c = 1
while c < 10:
    print(c)
    c += 1 #contador que impede o loop
print('FIM')"""

"""n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Você finalmente digitou o {}, obrigado!'.format(n))"""


"""soma = 0
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um número: '))
    resposta = str(input('Quer continuar? ')).upper()
    soma += n
print('FIM!Soma dos números: {}'.format(soma))"""

#Calculando par e ímpar:

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e'
      '\n{} números ímpares.'.format(par, impar))
