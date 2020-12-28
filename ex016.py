import math

catoposto = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = math.hypot(catoposto, catadj)
print('O valor da Hipotenusa é {:.2f}'.format(hipotenusa))

