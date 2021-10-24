numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha >= 0 and escolha <= 20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {numeros[escolha]}!')
