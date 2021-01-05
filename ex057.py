sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]

while sexo not in 'MmFm':
    sexo = str(input('Inválido! Digite o sexo da pessoa: ')).strip().upper()[0]
print('O sexo digitado foi: {}.'.format(sexo))
