num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

lista = []

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f'''O menor número é {min(lista)}
O maior número é {max(lista)}''')
