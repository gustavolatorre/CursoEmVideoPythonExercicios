from datetime import date

funcionario = dict()
anoAtual = date.today().year

funcionario['Nome'] = str(input('Nome: '))
funcionario['Idade'] = anoAtual - int(input('Ano de nascimento: '))
ctps = int(input('CTPS: (se não tiver digite 0) '))
if ctps != 0:
    funcionario['CTPS'] = ctps
    funcionario['Contratação'] = int(input('Ano de contratação: '))
    funcionario['Salário'] = float(input('Salário: R$'))
    funcionario['Aposentadoria'] = (35 - (anoAtual - funcionario['Contratação'])) + funcionario['Idade']
else:
    funcionario['CTPS'] = 0

print('=-'*25)
for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}')
