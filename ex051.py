primeiro = int(input('Digite um número para Calcular a PA: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao #Fórmula para calcular o enésimo termo da PA.
#Se for 20 primeiros, se troca o 10 por 20.
count = 0

for contador in range(primeiro, decimo + razao, razao):
    count += 1
    print('O {}º termo é {}'.format(count, contador))
print('FIM')
