num = int(input('Digite um número inteiro: '))
print('''[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num) [2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num) [2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num) [2:]}')
else:
    print('Opção inválida! Só é possível escolher entre 1, 2 e 3.')
