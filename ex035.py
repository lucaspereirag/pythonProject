cateto1 = float(input('Digite a primeira reta: '))
cateto2 = float(input('Digite a segunda reta: '))
base = float(input('Digite a terceira reta: '))

if cateto1 + cateto2 > base:
    print('Pode formar um triângulo')
else:
    print('Não é possível formar um triângulo')