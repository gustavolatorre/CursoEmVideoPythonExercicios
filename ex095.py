jogador = dict()
jogadores = list()
partidas = list()

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))

    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)

    jogadores.append(jogador.copy())

    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('Responda APENAS S ou N...')
    if opcao == 'N':
        break

print('=-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para para) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO... Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}: ')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols!')
    print('-' * 40)
print('VOLTE SEMPRE!')
