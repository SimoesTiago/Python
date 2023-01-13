frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = ''
for letra in range(len(tudojunto) - 1, -1, -1):
    inverso = inverso + tudojunto[letra]
print('Você digitou a frase {}, seu inverso é {}'.format(tudojunto, inverso))
if inverso == tudojunto:
    print('E um PALÍNDROMO!')
else:
    print('NÃO é um palíndromo.')

#apos junto
#inverso = junto[::-1] << Fatiamento, sem for
