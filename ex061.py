numero = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
fim = False
c = 0
pa = 0
while c < 10:
    print('O {}º termo da PA é: {}'.format(c + 1, numero))
    pa = numero + razao
    numero = pa
    c += 1
print('\nfim')
