from moeda import moeda, metade, dobro, aumentar
preco = int(input('Digite o preço: R$'))
print(f'A metade de {moeda(preco)} é {moeda(metade(preco))}')
print(f'O dobro de {moeda(preco)} é {moeda(dobro(preco))}')
print(f'Aumentando 10%, temos {moeda(aumentar(preco, 10))}')
