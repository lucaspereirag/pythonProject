from datetime import date
maioridade = 21
hoje = date.today().year
countMaior = 0
countMenor = 0
for c in range(0, 7):
    nascimento = int(input('Digite o ano de nascimento do {}: '.format(c + 1)))
    if hoje - nascimento > maioridade:
        countMaior += 1
    else:
        countMenor += 1
print('O total de maiores: {} '
       '\nO total de menores: {}'.format(countMaior, countMenor))