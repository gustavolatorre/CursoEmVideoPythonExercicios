import random
import time

print('=-'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('=-'*30)

num_computador = random.randint(0, 5)
num_jogador = int(input('Em que número pensei? '))

print('Processando...')
time.sleep(2)

if num_jogador == num_computador:
  print('PARABÉNS! Você conseguiu me vencer!')
else:
  print(f'GANHEI! Eu pensei no número {num_computador} e não no {num_jogador}!')
