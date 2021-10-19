soma = 0
media = 0
maior_homem = 0
nome_homem = ''
mulher_total20 = 0

for i in range(1, 5):
    print(f'----- {i} PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma = soma + idade
    if i == 1 and sexo == 'M':
        maior_homem = idade
        nome_homem = nome
    if sexo == 'M' and idade > maior_homem:
        maior_homem = idade
        nome_homem = nome
    if sexo == 'F' and idade < 20:
        mulher_total20 = mulher_total20 + 1

media = soma / 4

print(f'''A média de idade do grupo é {media:.2f} anos
O homem mais velho tem {maior_homem} anos e se chama {nome_homem}
Ao todo são {mulher_total20} mulher(es) com menos de 20 anos''')
