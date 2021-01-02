"""Cálculo do IMC - Índice de Massa Corpórea"""

pergunta1 = str(input('Você sabe o que é o IMC? '
                      '\n[1] Sim'
                      '\n[2] Não'
                      '\nSelecione: ')).strip()

if pergunta1 == '2':
    print('O IMC (Índice de Massa Corporal) é um cálculo '
          'que ajuda a avaliar se a pessoa está dentro do '
          'seu peso ideal, de acordo com a altura.')

pergunta2 = str(input('Vamos calcular ou seu IMC?'
                          '\n[1] Sim'
                          '\n[2] Não'
                          '\nSelecione: ')).strip()
if pergunta2 == '1':
        peso = float(input('Digite seu peso em kgs: '))
        altura = float(input('Digite sua altura em metros: '))
        IMC = (peso / (altura * altura))
        print('Você tem o IMC de {:.2f} kg/m². \n'.format(IMC), end='')
        if IMC < 18.5:
            print('Situação: Abaixo do Peso.')
        elif 18.5 <= IMC <= 25.0:
            print('Situação: Peso Ideal.')
        elif 25.0 <= IMC <= 30.0:
            print('Situação: Sobrepeso.')
        elif 30.0 <= IMC <= 40.0:
            print('Situação: Obesidade.')
        else:
            print('Situação: Obesidade Mórbida.')
else:
        print('Você deveria calcular o seu IMC!')