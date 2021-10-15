import random
import time

print('''SUAS OPÇÕES:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')

jogador = int(input('Qual é a sua opção? '))
computador = random.randint(1, 3)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')

if computador == 1:
    var = 'PEDRA'
elif computador == 2:
    var = 'PAPEL'
else:
    var = 'TESOURA'

if jogador == 1:
    var2 = 'PEDRA'
elif jogador == 2:
    var2 = 'PAPEL'
else:
    var2 = 'TESOURA'

print('=-'*12)
print(f'''Computador jogou {var}
Jogador jogou {var2}''')
print('=-'*12)

if jogador == 1 and computador == 3:
    print('VENCEU!')
elif jogador == 1 and computador == 2:
    print('PERDEU!')
elif jogador == 2 and computador == 1:
    print('VENCEU!')
elif jogador == 2 and computador == 3:
    print('PERDEU!')
elif jogador == 3 and computador == 1:
    print('PERDEU!')
elif jogador == 3 and computador == 2:
    print('VENCEU!')
elif jogador == computador:
    print('EMPATE!')
