termo = int(input('Primeiro termo: '))
f1 = 0
f2 = 1
contador = 3

print(f'{f1} -> {f2}', end='')

while contador <= termo:
    f3 = f1 + f2
    print(f'-> {f3}', end='')
    f1 = f2
    f2 = f3
    contador += 1
print(' -> FIM!')