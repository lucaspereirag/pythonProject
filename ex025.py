nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome {} ...'.format(nome))
analiseNome = 'SILVA' in nome.upper()
print(analiseNome)
#sem necessidade de varíavel:
print('Seu nome {} {} Silva no nome.'.format(nome, 'SILVA' in nome.upper()))
print('Seu nome {} tem Silva no nome?\n{}'.format(nome, 'silva' in nome.lower()))

