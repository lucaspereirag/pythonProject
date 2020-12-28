#import math
from math import sqrt, ceil, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz do {} é igual a {:.2f}'.format(num, ceil(raiz)))
print('A raíz do {} é igual a {:.2f}'.format(num, floor(raiz)))