from random import randint

print('JOGO: PAR OU ÍMPAR!')

contador = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}.', end='')
    print(' DEU PAR!' if soma % 2 == 0 else ' DEU ÍMPAR!')

    if escolha == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    if escolha == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('=-' * 25)

print(f'GAME OVER! Você venceu {contador} vez.')
