import math

angulo = float(input('Digite o ângulo desejado: '))

print(f'''O ângulo de {angulo} tem o SENO de {math.sin(math.radians(angulo)) :.2f}
O ângulo de {angulo} tem o COSSENO de {math.cos(math.radians(angulo)) :.2f}
O ângulo de {angulo} tem a TANGENTE de {math.tan(math.radians(angulo)) :.2f}''')
