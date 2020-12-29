viagem = float(input('Digite a distância da viagem: '))

if viagem <= 200:
    print('O valor da viagem será de: R$ {:.2f}'.format(viagem * 0.50))
else:
    print('O valor da viagem será de: R$ {:.2f}'.format(viagem * 0.45))