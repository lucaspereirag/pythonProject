salario = float(input('Digite seu salário: '))

if salario >= 1250:
    print('Seu salário corrigido será de: R$ {}'.format((salario * 0.10) + salario))
else:
    print('Seu salário corrigido será de R$ {}'.format((salario * 0.15) + salario))