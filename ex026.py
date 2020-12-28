frase = str(input('Digite uma frase qualquer: ')).strip()

print('A) A sua frase tem {} letras A '.format(frase.upper().count('A')))

print('B) Na sua frase, a letra A aparece pela primeira vez na posição nº {}'
      .format(frase.upper().find('A')+1))

print('C) Na sua frase, a última vez que aparece é na posição: {}'
      .format(frase.upper().rfind('A')+1))