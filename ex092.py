from datetime import date
hoje = date.today().year

individuo = {}
tempo = 35

individuo['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de Nascimento: '))
idade = hoje - anoNascimento
individuo['idade'] = idade
individuo['ctps'] = int(input('Número da Carteira de Trabalho(0 não possui): '))
if individuo['ctps'] != 0:
    individuo['contratacao'] = int(input('Digite ano da contratação: '))
    individuo['salario'] = float(input('Salário: R$ '))
    individuo['aposentadoria'] = (individuo['contratacao'] + 35) - hoje + idade

print('-=' * 25)

for k, v in individuo.items():
    print(f'  - {k} tem o valor {v}')







