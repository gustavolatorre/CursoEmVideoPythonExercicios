from random import randint

print('-='*20)
print('     GERADOR DE JOGOS MEGA SENA     ')
print('-='*20)

jogosMegaSena = []
jogosTemporarios = []
total = 1

quantidadeDeJogos = int(input('Quantos jogos você quer que eu sorteie? '))

while total <= quantidadeDeJogos:
    contador = 0
    while True:
        numeros = randint(1, 60)
        if numeros not in jogosTemporarios:
            jogosTemporarios.append(numeros)
            contador += 1
        if contador >= 6:
            break

    jogosTemporarios.sort()
    jogosMegaSena.append(jogosTemporarios[:])
    jogosTemporarios.clear()
    total += 1

print(f'***** Sorteando {quantidadeDeJogos} jogos *****')

for i, j in enumerate(jogosMegaSena):
    print(f'Jogo {i+1}: {j}')