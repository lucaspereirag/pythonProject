sacar = int(input('Digite um valor a sacar: R$ '))
#cédulas:
cem = 100
cinq = 50
vinte = 20
dez = 10
cinco = 5
um = 1
contcem = contcinq = contvinte = contdez = contcinco = contum = 0
#contador:
cont = 0
sacado = 0

while True:
    while sacar >= cem:
        sacar -= cem
        contcem += 1
    if contcem >= 1:
        print(f'Total de {contcem} cédulas de R$ 100')
    while sacar >= cinq:
        sacar -= cinq
        contcinq += 1
    if contcinq >= 1:
        print(f'Total de {contcinq} cédulas de R$ 50')
    while sacar >= vinte:
        sacar -= vinte
        contvinte += 1
    if contvinte >= 1:
        print(f'Total de {contvinte} cédulas de R$ 20')
    while sacar >= dez:
        sacar -= dez
        contdez += 1
    if contdez >= 1:
        print(f'Total de {contdez} cédulas de R$ 10')
    while sacar >= cinco:
        sacar -= cinco
        contcinco += 1
    if contcinco >= 1:
        print(f'Total de {contcinco} cédulas de R$ 5')
    while sacar >= um:
        sacar -= um
        contum += 1
    if contum >= 1:
        print(f'Total de {contum} cédulas de R$ 1')
    if sacar == 0:
        break