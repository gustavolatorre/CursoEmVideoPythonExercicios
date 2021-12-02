def ajuda(com):
    titulo(f'Acessando o manual do camando {com}')
    help(com)


def titulo(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')
