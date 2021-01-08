print('-'* 35)
print('{:^35}'.format('LG Bank $$ v2.0'))
print('-' * 35)

sacar = int(input('Digite o valor a sacar: '))
cedula = 100
contCedula = 0

while True:
    while sacar >= cedula:
        sacar -= cedula
        contCedula += 1
        print(f'O total de cédulas de {cedula} foi de {contCedula}.')
        if sacar >= cedula:
            cedula = 50
        elif sacar >= cedula:
            cedula = 20
        elif sacar >= cedula:
            cedula = 10
        elif sacar >= cedula:
            cedula = 5
        elif sacar >= cedula:
            cedula = 1
        if sacar == 0:
            break
