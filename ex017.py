import math

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Compirmento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa vai medir {hipotenusa :.2f}')
