num = int(input("Digite o número para calcular seu fatorial: "))
contador = num
fatorial = 1

print(f'{num}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print(f'{fatorial}')
