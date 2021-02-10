def introducao():
    """
    Retorna um painel verde iniciando o sistema.
    :return:
    """
    cor = ['\033[m',  # 0 - Limpa
           '\033[42m',  # 1 - Verde
           '\033[46m',  # 2 - Azul
           '\033[7;40m',  # 3 - Negativo Branco
           '\033[34m'  # 4 - Azul Thanks
           ]
    into = "Sistema de Ajuda PyHelp"
    intoN = len(into) + 4
    print(f'{cor[1]}', end='')
    print('~' * intoN)
    print(f'  {into}  ')
    print(f'~' * intoN)
    print(f'{cor[0]}')

def funcao():
    """
    Executa um painel solicitando uma função
    Retorna a descrição da função na tela.
    :return:
    """
    cor = ['\033[m',  # 0 - Limpa
           '\03342m',  # 1 - Verde
           '\033[46m',  # 2 - Azul
           '\033[7;40m',  # 3 - Negativo Branco
           '\033[34m',  # 4 - Azul Thanks
           ]
    from time import sleep
    while True:
        sleep(0.2)
        pergunta = str(input('Função ou Biblioteca: ')).strip().lower()
        print()
        sleep(0.5)
        if pergunta == 'fim':
            break
        acesso = f"Acessando o manual de {pergunta}"
        acessoN = len(acesso) + 4
        print(f'{cor[2]}', end='')
        print('~' * acessoN)
        print(f'  {acesso}  ')
        print(f'~' * acessoN)
        print(f'{cor[0]}', end='')
        sleep(1)
        print(f'{cor[3]}')
        print(help(pergunta))
        print(f'{cor[0]}')
        pergunta = ''
        sleep(1.5)
    print(f'{cor[4]}Obrigado por utilizar o PyHelp!;D{cor[0]}')



introducao()
funcao()