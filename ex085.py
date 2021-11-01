lista = []
par = []
impar = []


for i in range(1, 8):
    lista.append(int(input(f'Digite o {i} número: ')))

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'\nOs valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')
