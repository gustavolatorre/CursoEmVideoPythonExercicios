num = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{num} x {i:2} = {num * i}')
