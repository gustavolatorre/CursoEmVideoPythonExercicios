from datetime import date

ano_atual = date.today().year
contador1 = 0
contador2 = 0

for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i} pessoa: '))
    if (ano_atual - ano) >= 18:
        contador1 = contador1 + 1
    else:
        contador2 = contador2 + 1

print(f'''Ao todo tivemos {contador1} pessoa(s) maior(es) de idade!
E também tivemos {contador2} pessoa(s) menor(es) de idade!''')
