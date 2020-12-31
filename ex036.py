"""Programa para calcular empréstimo da casa"""

valor = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$ '))
anos = int(input('Digite em quantos anos: '))

parcelas = valor / (anos * 12)

print('Parcelas no valor de R$ {:.2f}'.format(parcelas))

if parcelas > (salario * 0.30):
    print('\nO seu salário em 30% é de R$ {:.2f}'.format(salario * 0.30))
    print('Não é possível realizar o empréstimo.'
          '\nFaltam R$ {:.2f}'.format((salario * 0.30) - parcelas))
else:
    print('\nVocê pode realizar o empréstimo.')
    print('O seu salário em 30% é de R$ {:.2f}'
          '\nPortanto, te sobra R$ {:.2f}'
          .format(salario * 0.30, (salario * 0.30) - parcelas))