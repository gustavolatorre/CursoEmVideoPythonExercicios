import datetime

nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos!')

if idade < 18:
    print(f'''Ainda faltam {18 - idade} ano(s) para o alistamento!
Seu alistamento será em {ano_atual + (18 - idade)}.''')
elif idade > 18:
    print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
s