print('='*30)
print('TEM DE TUDO VGP')
print('='*30)

soma = 0
contador = 0
contador2 = 0
menor = 0
nome_produto = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    soma += preco
    contador += 1
    if preco > 1000:
        contador2 += 1
    if contador == 1:
        nome_produto = produto
        menor = preco
        if preco < menor:
            menor = preco
            nome_produto = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

print('FIM DO PROGRAMA!')
print(f'''O total da compra foi de R${soma:.2f}
Temos {contador2} produto(s) custando mais de R$1000.00
O produto mais barato foi a {nome_produto} que custa R${menor:.2f}''')
