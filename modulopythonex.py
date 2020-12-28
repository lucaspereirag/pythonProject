#import math

from math import trunc

numreal = float(input(('Digite o número: ')))
print('O valor digitado foi {}. A porção inteira desse número é: {}'
      .format(numreal, trunc(numreal)))
