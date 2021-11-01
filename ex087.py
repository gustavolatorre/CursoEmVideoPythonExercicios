matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
print(f'\nA soma dos valores pares é {soma_par}!')

soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}!')

print(f'O maior número da segunda linha é {max(matriz[1])}!')
