resposta = 'S'
soma = 0
contador = 0
maior = 0
menor = 0
media = 0

while resposta in 'S':
    num = int(input('Digite um número: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    contador += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / contador

print(f'Você digitou {contador} números e a média foi de {media:.2f}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
