numero = int(input('Digite um número para calcularmos o fatorial: '))
atingiu = False
fatorial = 0
proximo = numero

while atingiu != True:
    fatorial = numero * (proximo - 1)
    numero = fatorial
    proximo -= 1
    if proximo == 1:
       atingiu = True

print('Fatorial: {}'.format(fatorial))




print('FIM')