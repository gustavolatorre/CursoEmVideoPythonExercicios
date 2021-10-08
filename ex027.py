nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split(' ')

print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {lista[0]}
Seu último nome é {lista[-1]}''')
