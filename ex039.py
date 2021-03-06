"""Cálculo da Idade para Alistamento Militar"""
from datetime import date

anoAtual = date.today().year

sexo = int(input('Qual o seu sexo?'
                 '\nEscolha as opções'
                 '\n[1]Masculino '
                 '\n[2]Feminino' 
                 '\nSelecione: '))

if sexo == 1:
    nascimento = int(input('Ano de Nascimento: '))
    idade = anoAtual - nascimento
    alistamento = nascimento + 18
    if idade < 16:
        print('Você tem {} anos de idade.'
              '\nFique tranquilo, você ainda tem tempo até se alistar.'
              '\nData prevista para {}'.format(idade, alistamento))
    elif 16 <= idade < 18:
        print('Você tem {} anos de idade.'
              '\nPrepare-se, você se alistará no exercícito em breve!'
              '\nVocê vai se alistar no ano de {}'.format(idade, alistamento))
    elif idade == 18:
        print('Você tem {} anos de idade.'
              '\nAtenção! Está na hora de alistar.'.format(idade))
    else:
        print('Você tem {} anos de idade.'
              '\nVocê já passou do tempo de se alistar.'
              '\nVocê já se alistou/deveria ter se alistado no ano de {}'
              .format(idade, alistamento))
else:
    print('Seu alistamento não é necessário, obrigado.')
