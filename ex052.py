num = int(input('Digite um número: '))
contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=' ')
        contador = contador + 1

print(f'\nO número {num} foi divisível {contador} vezes!')

if contador == 2:
    print('Por isso ele é um número PRIMO!')
else:
    print('Por isso ele NÃO é um número PRIMO!')
