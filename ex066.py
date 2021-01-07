num = soma = cont = 0

while True:
    num = int(input('Digite um número [999 Encerra o programa]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} é: {soma}')