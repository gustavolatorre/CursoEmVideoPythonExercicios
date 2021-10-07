dias_aluguel = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))
valor_aluguel = (60 * dias_aluguel) + (km_rodados * 0.15)

print(f'O total a pagar é de R${valor_aluguel :.2f}.')
