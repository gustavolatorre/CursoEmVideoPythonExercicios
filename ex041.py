import datetime

nascimento = int(input('Digite o ano de nascimento: '))

ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

print(f'O atleta tem {idade} anos!')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
