lista = []

while True:
    num = (int(input('Digite um valor: ')))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Vou excluir!')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer contimuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print('-*'*20)
print(f'Você digitou os valores: {sorted(lista)}')
