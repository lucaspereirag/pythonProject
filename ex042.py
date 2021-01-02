cateto1 = float(input('Digite a primeira reta: '))
cateto2 = float(input('Digite a segunda reta: '))
base = float(input('Digite a base: '))

if cateto1 + cateto2 > base:
    print('Pode formar um triângulo. ', end='')
    if cateto1 == cateto2 == base:
        print('Seu triângulo é EQUILÁTERO, todos os lados iguais.')
    elif cateto1 == cateto2 or cateto1 == base or cateto2 == base:
        print('Seu triângulo é ISÓSCELES, com dois lados iguais.')
    else:
        print('Seu triângulo é ESCALENO, nenhum lado é igual.')
else:
    print('Não é possível formar um triângulo')
