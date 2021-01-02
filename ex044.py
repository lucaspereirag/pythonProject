"""Cálculo do Preço do Produto e Formas de Pagamento"""

preco = float(input('Digite o preço do produto: R$ '))
pagamento = int(input('Forma de pagamento: '
                      '\n[1] À vista com dinheiro'
                      '\n[2] Cheque'
                      '\n[3] À vista no cartão'
                      '\n[4] Em até 2x no cartão'
                      '\n[5] A partir de 3x ou mais no cartão'
                      '\nSelecione: '))
if pagamento == 1 or pagamento == 2:
    if pagamento == 1:
        print('Voçê selecionou a opção Pagamento À vista com dinheiro'
          '\nO valor a pagar é de R$ {:.2f}'.format(preco - (preco * 0.10)))
    else:
        print('Voçê selecionou a opção Pagamento em Cheque'
          '\nO valor a pagar é de R$ {:.2f}'.format(preco - (preco * 0.10)))
elif pagamento == 3:
    print('Você seleciou a opção Pagamento À vista no Cartão'
          '\nO valor a pagar é de R$ {:.2f}'.format(preco - (preco * 0.05)))
elif pagamento == 4:
    print('Você selecionou a opção Pagamento em até 2x no Cartão'
          '\nO valor a pagar é de R$ {:.2f}'
          '\nCada parcela no valor de R$ {:.2f}'.format(preco, preco / 2))
else:
    print('Você selecionou a opção Pagamento em 3x ou mais no Cartão'
          '\nJuros de R$ {:.2f}'
          '\nO valor a pagar é de R$ {:.2f}'
          .format(preco * 0.20, preco + (preco * 0.20)))
    parcelas = int(input('Digite o valor de parcelas: '))
    if parcelas < 3:
        print('Erro! Não pode Parcelar menor que 3x. Operação Cancelada.')
    else:
        print('O valor de cada parcela é de R$ {:.2f}'.format((preco + (preco * 0.20)) / parcelas))

print('Obrigado e volte sempre!')
