import random


print('=-'*30)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('=-'*30)

num_computador = random.randint(0, 11)
num_jogador = int(input('Em que número pensei? '))
contador = 1

while num_jogador != num_computador:

  contador = contador + 1

  if num_jogador == num_computador:
    print('PARABÉNS! Você conseguiu me vencer!')
  else:
    if num_jogador > num_computador:
      print('Menos... Tente outra vez.')
    if num_jogador < num_computador:
      print('Mais... Tente outra vez.')

  num_jogador = int(input('Qual é o seu novo palpite? '))

print(f'Acertou com {contador} tentativas!')
