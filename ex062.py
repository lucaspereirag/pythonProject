p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos = int(input('Qtd Termos: '))

while termos > 0:
    print(p_termo, end=' ')
    p_termo += razao
    termos -= 1
    if termos == 0:
        termos = int(input('\nAcrescentar mais números na sequência: '))