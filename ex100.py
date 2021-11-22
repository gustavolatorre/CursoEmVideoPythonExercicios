from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
    for i in lista:
        print(f'{i} ', end='')
    print('PRONTO!')

def soma(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}!')


numeros = list()

sorteia(numeros)
soma(numeros)
