lista_completa = []
lista_par = []
lista_impar = []
while True:
    lista_completa.append(int(input('Digite um valor: ')))
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
for i in lista_completa:
    if i % 2 == 0:
        lista_par.append(i)
    if i % 2 == 1:
        lista_impar.append(i)
print(f'A lista completa é: {lista_completa}')
print(f'A lista de pares é: {lista_par}')
print(f'A lista de imparares é: {lista_impar}')
