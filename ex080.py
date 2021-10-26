lista = []

for i in range(0, 5):
    num = int(input('Digite um número: '))
    if i == 0:
        lista.append(num)
        print('Adicionado no final da lista!')
    elif num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista!')
    else:
        contador = 0
        while contador < len(lista):
            if num <= lista[contador]:
                lista.insert(contador, num)
                print(f'Adicionado na posição {contador} da lista')
                break
            contador += 1
print('=*'*25)
print(f'Os valores digitados foram {lista}')
