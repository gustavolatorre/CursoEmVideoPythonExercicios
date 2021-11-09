def area(a, b):
    area = a * b
    print(f'A área de um terreno {a}x{b} é de {area:.2f}m².')


print(' Controle de terrenos')
print('-'*25)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
