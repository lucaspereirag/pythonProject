numero = int(input('Primeiro Número: '))
sequencia = int(input('Quantos números na sequência Fibonacci: '))
count = 0
antecessor = 0
sucessor = 0

while sequencia > count:
    if numero == 1:
        print('{} -> '.format(numero), end='')
    print('{} -> '.format(numero), end='')
    antecessor = numero - antecessor
    numero = numero + antecessor
    count += 1
print('FIM')
