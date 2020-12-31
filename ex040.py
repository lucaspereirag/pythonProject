"""Cálculo da Média do Aluno na escola"""
from statistics import mean
from time import sleep
from math import ceil

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# media = (nota1 + nota2) / 2 Não use!
media = mean([nota1, nota2])

print('A média do aluno foi de: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado!')
elif 5.0 <= media < 7.0:
    print('Aluno em Recuperação!')
    print('Aluno está em recuperação')

    nota3 = ceil(float(input('Digite o valor da Nota da Prova de Recuperação: ')))

    if nota3 >= 7.0:
        print('Parabéns, você recuperou a nota!'
              '\nSua nota foi de {}'
              '\nAluno aprovado!'.format(nota3))
    else:
        print('Não recuperou a nota, aluno reprovado.')
else:
    print('Sua média foi inferior a 5.0'
          '\nReprovado.')
