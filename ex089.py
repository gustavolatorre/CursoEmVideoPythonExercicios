alunos = []
alunoProvisorio = []
media = 0

while True:
    opcao = ' '

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunoProvisorio.append(nome)
    alunoProvisorio.append(nota1)
    alunoProvisorio.append(nota2)
    alunoProvisorio.append(media)

    alunos.append(alunoProvisorio[:])
    alunoProvisorio.clear()

    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*13)
for indice, x in enumerate(alunos):
    print(f'{indice:<4}{x[0]:<10}{x[3]:>8}')

while True:
    print('-=' * 13)
    escolhaAluno = int(input('Mostrar notas de qual aluno? (999 para interromper) '))
    if escolhaAluno == 999:
        print('Finalizando o programa!')
        break
    if escolhaAluno <= len(alunos) - 1:
        print(f'Notas de {alunos[escolhaAluno][0]} são: {alunos[escolhaAluno][1:3]}')
