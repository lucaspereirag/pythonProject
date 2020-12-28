from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do Ângulo: '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print('O valor do Cosseno é {:.2f} \nSeno {:.2f} \nTangente é {:.2f}'
      .format(cosseno, seno, tangente))