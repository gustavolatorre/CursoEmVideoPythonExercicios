def aumentar(valor, pctAumento, format=False):
    resultado = valor + (valor * (pctAumento/100))
    return resultado if format is False else moeda(resultado)


def diminuir(valor, pctDiminuir, format=False):
    resultado = valor - (valor * (pctDiminuir/100))
    return resultado if format is False else moeda(resultado)


def dobro(valor, format=False):
    resultado = valor * 2
    return resultado if format is False else moeda(resultado)


def metade(valor, format=False):
    resultado = valor / 2
    return resultado if format is False else moeda(resultado)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor, pctAumento, pctDiminuir):
    print('=-'*15)
    print(f'{"Resumo do valor":^30}')
    print('=-' * 15)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{pctAumento}% de aumento: \t{aumentar(valor, pctAumento, True)}')
    print(f'{pctDiminuir}% de redução: \t{diminuir(valor, pctDiminuir, True)}')
    print('=-' * 15)
