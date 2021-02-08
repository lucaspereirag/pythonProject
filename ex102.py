def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número.
    Se 'show' True,então mostra o cálculo.
    :param num: O número a calcular
    :param show: (Opcional) Mostra ou não a conta
    :return: O valor do fatorial de um número "num".
    """
    num = int(input('Digite um número: '))
    i = 1
    for c in range(num, 0, -1):
        i *= c
    if show == True:
        for c in range(num, 0, -1):
            print(f'{c}{" x " if c > 1 else " = "}', end='')
    return i

print(fatorial(5, show=True))
fatorial(5)

