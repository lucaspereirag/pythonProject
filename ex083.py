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
    print('\033[31mERRO! Tem um "(" a mais.\033[m')
elif countsegundo > countprimeiro:
    print('\033[33mERRO! Tem um ")" a mais.\033[m')
else:
    print('\033[32mSua expressão é válida!\033[m')