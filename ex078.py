lista = []
maior = 0
menor = 0

for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('-='*20)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(indice, end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(indice, end=' ')
