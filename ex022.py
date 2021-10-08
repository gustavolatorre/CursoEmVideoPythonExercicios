nome = str(input('Digite seu nome completo: ')).strip()
lista_nome = nome.split()

print(f'''Analisando seu nome...
Seu nome em maiúsculo é {nome.upper()}
Seu nome em minúsculo é {nome.lower()}
Seu nome tem ao todo {len(nome) - nome.count(' ')} letras
Seu primeiro nome é {lista_nome[0]} e ele tem {nome.find(' ')} letras''')
