soma = 0
contador= 0

for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        contador = contador + 1
        soma = soma + i

print(f'A soma de todos os {contador} números ímpares múltiplos de 3 no intervalo de 1 até 500 é de {soma}.')