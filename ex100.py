from random import randint

numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numeros.append(randint(0, 10))
    for i in numeros:
        print(f'{i} ', end='')
    print('PRONTO!')

def soma(n):
    soma = 0
    for i in n:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {n}, temos {soma}!')


sorteia()
soma(numeros)
