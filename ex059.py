from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

soma = 0
multiplicar = 0
maior = 0
opcao = 0

while opcao != '5':
    print('========================')
    print('''MENU:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    opcao = str(input('Qual é a sua opção? '))

    if opcao == '1':
        soma = num1 + num2
        print(f'{num1} + {num2} = {soma}')
    if opcao == '2':
        multiplicar = num1 * num2
        print(f'{num1} x {num2} = {multiplicar}')
    if opcao == '3':
        if num1 > num2:
            maior = num1
            print(f'Entre {num1} e {num2} o maior é {maior}')
        if num2 > num1:
            maior = num2
            print(f'Entre {num1} e {num2} o maior é {maior}')
        if num1 == num2:
            print(f'entre {num1} e {num2} não existe maior, pois são iguais!')
    if opcao == '4':
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    if opcao == '5':
        print('Finalizando...')
        sleep(2)
        print('Fim do programa! Volte sempre!')
