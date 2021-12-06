def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número!')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número!')
            return 0
        else:
            return n


num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFloat('Digite um valor real: ')
print(f'O valores digitados foram {num1} e {num2}')
