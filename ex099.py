def maior(* num):
    contador = 0
    maior = 0
    print('=-'*15)
    print('Analisando os valores...')
    for i in num:
        print(f'{i} ', end='')
        if contador == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        contador += 1
    print(f'\nForam informados {contador} valores.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
