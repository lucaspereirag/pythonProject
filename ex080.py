lista = []
#pegar o último valor da lista: lista[len(lista) - 1] -> Na lista, a última posição
# OU : lista[-1]

for contador in range(0, 5):
    numero = int(input(f'Digite um número {contador}: '))
    if contador == 0 or numero > lista[-1]:#Se o nº for a primeira vez ou se os próximos
        #forem maiores que o que já está na ultima posição, adiciona na última posição.
        lista.append(numero)
    else:
        pos = 0 #se o nº não é o primeiro e nem é maior que o último, assumo zero
        while pos < len(lista): #enquanto a posição for menor que o tamanho da lista:
            if numero <= lista[pos]: #se o número digitado for menor igual a posição da lista,
                lista.insert(pos, numero)#insere esse número nessa posição percorrida
                break#após achar a posição, break o While e volta ao Input na linha 8
            pos += 1 #após, a posição ganha contador.

print('-=' * 30)
print(f'A lista em ordem crescente sem Sort: {lista}')

