velocidade = int(input('Qual é a velocidade do carro? '))
multa = (velocidade - 80) * 7.0

if velocidade <= 80:
  print('Tenha um bom dia! Dirija com seguraça!')
else:
  print(f'''MULTADO! Você excedeu o limite permitido de 80 km/h
Você deve pagar uma multa no valor de R${multa :.2f}!
Tenha um bom dia! Dirija com seguraça!''')
