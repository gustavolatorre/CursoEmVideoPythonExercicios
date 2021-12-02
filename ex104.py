def leiaInt(msg):
    correto = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            correto = True
        else:
            print('ERRO! Digite um número inteiro válido!')
        if correto:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
