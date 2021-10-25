from random import randint

num = tuple(randint(i + 0, 10) for i in range(randint(5, 5)))
print('Os valores sorteados foram: ', end=' ')
for i in num:
    print(i, end=' ')
print(f'\nO maior valor sorteado foi o {max(num)}')
print(f'O menor valor sorteado foi o {min(num)}')
