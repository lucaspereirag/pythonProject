import random
from time import sleep

numint = random.randint(0, 5) #Computador emite um número aleatório
#print(numint)
print('-=-' * 20)
numUser = int(input('Digite um número entre 0 e 5: ')) #Usuário digita um número aleatório
print('-=-' * 20)
print('Processando os dados...')
sleep(1)
if numUser == numint: #Faz a Validação entre Computador x Usuário
    print('Seu número {} é igual ao {} escolhido pelo computador. \nParabéns!'
          .format(numUser, numint))
else:
    print('Seu número {} não é o mesmo número {} que o computador escolheu. \nTente novamente!'
          .format(numUser, numint))