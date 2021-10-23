contador_18 = 0
contador_homem = 0
contador_mulher = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if idade >= 18:
        contador_18 += 1
    if sexo in 'M':
        contador_homem += 1
    if sexo in 'F' and idade < 20:
        contador_mulher += 1
    if continuar in 'N':
        break
        
print(f'''Total de pessoas com mais de 18 anos: {contador_18}
Ao todo temos {contador_homem} homem(ns) cadastrado(s).
E temos {contador_mulher} mulher(es) com menos de 20 anos.''')
