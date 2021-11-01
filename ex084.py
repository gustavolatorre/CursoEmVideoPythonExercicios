pessoas = []
dados = []
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'\nAo todo, você cadastrou {len(pessoas)} pessoas!')
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de: ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end='')
