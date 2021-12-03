import moeda
preco = int(input('Digite o preço: R$'))
print(f'A metade de R${preco:.1f} é R${moeda.metade(preco):.1f}')
print(f'O dobro de R${preco:.1f} é R${moeda.dobro(preco):.1f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preco, 10):.1f}')
