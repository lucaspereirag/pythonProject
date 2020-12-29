num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
    print('Número 1 é maior.')
elif num2 > num1 and num2 > num3:
    print('Número 2 é maior')
else:
    print('Número 3 é maior.')

if num1 < num2 and num1 < num3:
        print('Número 1 é menor.')
elif num2 < num1 and num2 < num3:
        print('Número 2 é menor')
else:
        print('Número 3 é menor.')

