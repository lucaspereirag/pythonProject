lista = []


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break

print('-=' * 25)
print('-'*25)
print('-'* 5, 'BOLETIM', '-' *5)
print('-'*25)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*25)
for indice, aluno in enumerate(lista):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno?(999 - Interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('Volte Sempre!!')