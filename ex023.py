numero = int(input('Digite um número entre 0 e 9999: '))
milhar = numero // 1000 % 10
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero // 1 % 10
print('Analisando o numero {}'.format(numero))
print('O valor do milhar: {}'.format(milhar))
print('O valor da centena: {}'.format(centena))
print('O valor da dezena: {}'.format(dezena))
print('O valor da unidade: {}'.format(unidade))



"""n2 = str(int(10000 + n))
print('O número {} milhar, {}'.format(n, n2[1]))
print('O número {} centena, {}. '.format(n, n2[2]))
print('O número {} dezena, {}. '.format(n, n2[3]))
print('O número {} unidade, {}.'.format(n, n2[4]))"""