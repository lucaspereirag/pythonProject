contador = 0

#utilizando o while "Padrão"
"""while contador <= 10:
    print(contador, '...', end='')
    contador += 1
print('Fim.')"""

#se remover o contador e deixar o True algo será executado para sempre:
"""while True:
    print(contador, '...', end='')
    contador += 1
print('Não tem fim.')"""

#o problema com flag:
"""numero = soma = 0
while numero != 999:
    numero = int(input('Digite um número: '))
    soma += numero
print('A soma dos números é: {}'.format(soma))"""

"""com loop infinito com o Break:
numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
#print('A soma dos números: {}'.format(soma))
print(f'A soma dos números: {soma}')"""


"""idade = 33
nome = 'José'
print(f'O {nome} tem {idade} anos.')#Python 3.6+
print('O {} tem {} anos.'.format(nome, idade))#Python 3.0
print('O %s tem %d anos.' %(nome, idade))#Python 2"""

nome = 'Lucas'
idade = 26
salário = 15000.14
print(f'O {nome:-^20} tem {idade} e ganha o salário de R$ {salário:.2f}')