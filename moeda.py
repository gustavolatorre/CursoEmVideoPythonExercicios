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
