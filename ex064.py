num = int(input('Digite um número [999 para parar]: '))

soma = 0
contador = 0

while num != 999:
    soma = soma + num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {contador} números e a soma entre eles foi de {soma}.')
