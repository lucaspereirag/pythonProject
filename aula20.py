'''def mostraLinha():
    print('-' * 30)

mostraLinha()
print('Olá, meu nome é Lucas!')
mostraLinha()
'''


'''def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


# Código Principal rolando:
mensagem('Sistema de Alunos')
mensagem('Posso chamar o parâmetro quantas vezes eu quiser')'''


'''def soma(a, b):
    print(f'A soma de A = {a} e a soma de B = {b}')
    soma = a + b
    print(f'A soma de A + B = {soma}')


#Programa Principal
soma(5, 5)
soma(10, 8)
soma(20, 1)
#soma(4) #passando apenas 1 parâmetro.'''
#soma(a=4, b=5)
'''soma(b=10, 20)
'''


'''def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


contador(2, 1, 7)
contador(5, 4, 1, 3, 10, 11, 15)
contador(1)'''



'''def contador(* num):
    tamanho = len(num)
    print(f'Recebi os números, sendo {num}, e são ao todos {tamanho} números.')


contador(2, 1, 7)
contador(5, 4, 1, 3, 10, 11, 15)
contador(1)'''


'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(valores)

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

def soma (* valores):
    soma = 0
    for numero in valores:
        soma += numero
    print(f'Somandos os valores {valores}, teremos a soma de {soma}')


soma(2, 4)
soma(3, 5, 2)
soma(1, 9, 10, 20, 30)








