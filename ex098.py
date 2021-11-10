def contagem(a, b, c):
    from time import sleep
    print('=-' * 20)
    print(f'Contagem de {a} até {b} em {abs(c)}')
    for i in range(a, b + c, c):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('Fim!')
    print('=-' * 20)


contagem(1, 10, 1)
contagem(10, 0, -2)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
