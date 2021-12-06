def linha(tamanho=42):
    return '=' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    contador = 1
    for i in lista:
        print(f'{contador} - {i}')
        contador += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao
