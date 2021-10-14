valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo_financiamento = int(input('Quantos anos de financiamento? '))

prestacao = tempo_financiamento * 12
valor_parcelas = valor_casa / prestacao

print(f'Para pagar uam casa de R${valor_casa:.2f} em {tempo_financiamento} anos a prestação será de R${valor_parcelas:.2f}')

if valor_parcelas > (salario * 0.30):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
