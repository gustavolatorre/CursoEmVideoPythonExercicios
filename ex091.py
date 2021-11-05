from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogador4': randint(1, 6)}

rank = dict()

print('Jogadas:')

for k, v in jogadas.items():
    print(f'{k} jogou {v} no dado!')
    sleep(1)

rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('-='*25)

print('RANKING JOGADORES:')

for i, v in enumerate(rank):
    print(f'{i+1}o. lugar: {v[0]} com {v[1]}!')
