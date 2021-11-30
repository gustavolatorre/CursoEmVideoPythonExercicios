def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do fatorial de um número num.
    """
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    if show == False:
       return print(fatorial)
    else:
        for i in range(num, 0, -1):
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' =', fat)


fatorial(5, show=True)
help(fatorial)
