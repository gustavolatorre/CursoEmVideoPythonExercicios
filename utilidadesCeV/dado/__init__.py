def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro: \"{entrada}\" é um preço inválido!')
        else:
            valido = True
            return float(entrada)


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
