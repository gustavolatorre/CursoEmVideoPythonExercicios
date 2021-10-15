print('~~~~~~~~~~LOJA X~~~~~~~~~~')

compra = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a sua opção? '))

if opcao == 1:
    valor = compra - (compra * 0.10)
elif opcao == 2:
    valor = compra - (compra * 0.05)
elif opcao == 3:
    prestacao = compra / 2
    valor = compra
    print(f'Sua compra será parcelada em 2x de R${prestacao:.2f} SEM JUROS!')
elif opcao == 4:
    qtde_parcela = int(input('Quantas parcelas? '))
    valor = compra + (compra * 0.20)
    prestacao = valor / qtde_parcela
    print(f'Sua compra será parcelada em {qtde_parcela}x de R${prestacao:.2f} COM JUROS!')
else:
    valor = 0
    print('Opção inválida! Tente novamente.')

print(f'Sua compra de R${compra:.2f} vai custar R${valor:.2f} no final.')
