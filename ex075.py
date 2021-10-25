num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número número: ')))

print(f'O número 9 apareceu {num.count(9)} vez(es)!')
if 3 in num:
       print(f'O número 3 está na posição {num.index(3)+1}!')
else:
       print('O número 3 não apareceu em nenhuma posição!')
print('Os valores pares digitados foram: ', end='')
for i in num:
       if i % 2 == 0:
              print(i, end=' ')
