peso = float(input('Qual é seu peso?(Kg) '))
altura = float(input('Qual é a sua altura?(m) '))

imc = peso / (altura * altura)

print(f'O IMC dessa pessoa é {imc:.1f}.')

if imc < 18.5:
    print('A pessoa está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('A pessoa está com o peso ideal!')
elif imc >= 25 and imc < 30:
    print('A pessoa está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('A pessoa está em obesidade!')
else:
    print('A pessoa está em obesidade mórbida!')
