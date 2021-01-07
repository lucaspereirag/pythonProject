cont = contIdade = contHomens = contMulher20 = 0

print('-=' * 15, '\nCadastro de Pessoas')
print('-=' * 15)

while True:
    idade = int(input('\033[1mDigite a idade:\033[m '))
    if idade >= 18:
        contIdade += 1
    sexo = ' '
    while sexo not in 'MmFf':
      sexo = str(input('\033[1mDigite o sexo [M/F]:\033[m ')).strip().upper()[0]
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulher20 += 1
    cont += 1
    print('-=' * 15)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\n\033[7mDeseja continuar? [S/N]:\033[m ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'\nQuantidade de pessoas cadastradas: {cont}'
      f'\nQuantidade de Pessoas maiores que 18: {contIdade}'
      f'\nQuantidade de Homens cadastrados: {contHomens}'
      f'\nQuantidade de Mulher menores de 20 anos: {contMulher20}')
