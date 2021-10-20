termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = termo
contador = 1

while contador <= 10:
    print(f'{pa}', end=' -> ')
    pa = pa + razao
    contador += 1

print('FIM!')
