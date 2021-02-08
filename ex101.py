def voto(nascimento):
    """
    Informa com base na idade, se o voto da pessoa é:
    Obrigatório, não obrigatório ou Opcional.
    :param idade: Pergunta a idade do usuário.
    """
    from datetime import date
    hoje = date.today().year

    idade = hoje - nascimento
    if idade < 16:
        print(f'Sua idade de {idade}, seu voto é Negado.')
    elif idade >= 18 and idade <= 65:
        print(f'Sua idade de {idade}, seu voto é obrigatório.')
    else:
        print(f'Sua idade de {idade}, seu voto é opcional')


#help(voto)
nascimento = int(input('Digite o ano de nascimento: '))
voto(nascimento)


