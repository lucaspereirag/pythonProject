nome = str(input('Digite seu nome: ')).title().strip()
if nome == 'Lucas':
    print('Seu nome é o mais bonito!')
elif nome in 'Laura Tony Nina':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é comum.')
print('Aliás, tenha um bom dia, \033[7m{}\033[m!'.format(nome))
