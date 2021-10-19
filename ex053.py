frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[i]

print(f'O inverso de {frase} é {inverso}!')

if inverso == junto:
    print('É um PALÍNDROMO')
else:
    print('NÃO é um PALÍNDROMO')
