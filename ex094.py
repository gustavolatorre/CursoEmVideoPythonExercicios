pessoa = dict()
pessoas = list()
soma = 0
media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite APENAS M ou F...')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    pessoas.append(pessoa.copy())
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if opcao in 'SN':
            break
        print('Responda APENAS S ou N...')
    if opcao == 'N':
        break

print('-='*30)
print(f'a) Ao todo temos {len(pessoas)} pessoas cadastradas!')
media = soma / len(pessoas)
print(f'b) A média de idade é de {media:.2f} anos!')
print(f'c) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]} ', end='')
print()
print(f'd) Lista das pessoas que estão acima da média: ', end='')
for p in pessoas:
    if p['Idade'] >= media:
        print('          ', end='')
        for k, v in p.items():
            print(f'\n{k} = {v} ', end='')
        print('\n--------------------')
print('\n-*-*-*-*ENCERRADO-*-*-*-*')
