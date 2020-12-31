"""Conversor de Inteiros"""
n1 = int(input('Digite o número inteiro a ser convertido: '))
print('''Escolha uma das opções para converter: '
      [1] Converte para Binário
      [2] Converte para Octal
      [3] Converte para Hexadecimal''')

opcao = int(input('Sua opção: '))

if opcao == 1:
#Conversor de Inteiros em binário
    print('O número {} convertido em binário é: {}'
      .format(n1, bin(n1)[2:]))
elif opcao == 2:
#Conversor de Inteiros em Octal
    print('O numero {} convertido em Octal é: {}'
      .format(n1, oct(n1)[2:]))
elif opcao == 3:
#Conversos de Inteiros em Hexadecimal
    print('O número {} convertido em Hexadecimal é: {}'
      .format(n1, hex(n1)[2:].upper()))
else:
    print('Opção Inválida, rode o programa novamente.')

