jogador = dict()
totalGols = 0
i = 1
lista_gols = list()

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

if partidas > 0:
    for i in range(1, partidas + 1):
        gol = int(input(f'Quantos gols na partida {i}? '))
        lista_gols.append(gol)
        totalGols += gol

jogador['Gols'] = lista_gols
jogador['Total'] = totalGols

print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}!')
print('=-'*30)
for i, v in enumerate(jogador['Gols']):
    print(f'-> Na partida {i + 1}, fez {v} gols!')
print(f'Foi um total de {jogador["Total"]} gols!')
