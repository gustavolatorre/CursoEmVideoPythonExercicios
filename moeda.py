def aumentar(valor, pctAumento):
    resultado = valor + (valor * (pctAumento/100))
    return resultado


def diminuir(valor, pctDiminuir):
    resultado = valor - (valor * (pctDiminuir/100))
    return resultado


def dobro(valor):
    resultado = valor * 2
    return resultado


def metade(valor):
    resultado = valor / 2
    return resultado


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
