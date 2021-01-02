from datetime import date

nascimento = int(input('Qual ano vcê nasceu? '))
hoje = date.today().year
idade = hoje - nascimento

print('Você tem {} anos. \nSua Classificação: '.format(idade))

if idade <= 9:
    print('Você está selecionado na categoria: Mirim')
elif idade <= 14:
    print('Você está selecionado na categoria: Infantil')
elif idade <= 19:
    print('Você está selecionado na categoria: Júnior')
elif idade <= 25:
    print('Você está selecionado na categoria: Sênior')
else:
    print('Você está selecionado na categoria: Master')