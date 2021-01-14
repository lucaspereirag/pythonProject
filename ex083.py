
palavras = []
countprimeiro = countsegundo = 0

palavras.append(str(input('Digite uma expressão: ')))

for p in palavras:
    for vogal in p:
        if vogal == '(':
            countprimeiro += 1
            #print(vogal, end='')
        elif vogal == ')':
            countsegundo += 1
            #print(vogal)
if countprimeiro > countsegundo:
    print('ERRO!Tem um "(" a mais.')
if countsegundo > countprimeiro:
    print('ERRO !Tem um ")" a mais.')
else:
    print('Sua expressão é válida!')