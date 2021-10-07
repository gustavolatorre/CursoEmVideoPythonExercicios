produto = float(input('Qual é o preço do prudto? R$'))
valor_desconto = produto - (produto * 0.05)


print(f'O produto que custava R${produto}, na promoção com desconto de 5% vai custar R${valor_desconto :.2f}.')
