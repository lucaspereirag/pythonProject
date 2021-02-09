def leiaint():
    numero = input('Digite um número: ')
    if numero.isnumeric():
        numero = int(numero)
        return numero
    else:
        while numero.isnumeric() == False:
            print(f'\033[031mErro, número {numero} não é inteiro.\033[m')
            numero = input('Digite um número: ')
            if numero.isnumeric():
                break
        return numero


n = leiaint()
print(f'O valor digitado foi: {n}')