palindromo = str(input('Digite uma frase: ')).strip().upper() #espaços eliminados
palavras = palindromo.split() #gerou uma lista
frase = ''.join(palavras) #juntou a lista sem espaço
inverso = frase[::-1]

print('O inverso de {} é {}'.format(frase, inverso))
if inverso == frase:
        print('A frase é um palíndromo!')
else:
        print('A frase não é um palíndromo')



#Solução com FOR:
palindromo2 = str(input('Digite uma frase: ')).strip().upper() #espaços eliminados
palavras2 = palindromo2.split() #gerou uma lista
frase2 = ''.join(palavras2) #juntou a lista sem espaço
inverso2 = '' #varrer a frase de trás pra frente
for letra2 in range(len(frase2) - 1, -1, -1):#esse RANGE,foi da última letra, até a primeira, voltando -1
    inverso2 += frase2[letra2]
print('O inverso de {} é {}'.format(frase2, inverso2))
if inverso2 == frase2:
        print('A frase é um palíndromo!')
else:
        print('A frase não é um palíndromo')