expressao = str(input('Digite a expressão: '))

lista1 = []
lista2 = []

for i in expressao:
    if i == '(':
        lista1.append('(')
    elif i == ')':
        lista2.append(')')

if len(lista1) == len(lista2):
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
