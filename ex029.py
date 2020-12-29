from time import sleep

limite = 80
velocidade = float(input('Valor do carro no radar: '))
print('Analisando velocidade...')
sleep(0.5)
if velocidade > limite:
    print('Você foi multado! Velocidade: {} km/h'.format(velocidade))
    print('Valor da multa de R$ {:.2f}'.format((velocidade - limite) * 7))
else:
    print('Boa viagem.')



