"""nome = str(input('Qual seu nome? '))
if nome == 'Lucas':
    print('Que nome lindo você tem!')
else:
    print('Seu nome não é tão bonito assim!')
print('Bom dia {}!'.format(nome))"""


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('Sua média foi de {}'.format(media))
if media >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua nota foi baixa, estude mais.')