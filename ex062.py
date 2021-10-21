termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

pa = termo
contador = 1
cont_aux = 1
total = 0
opcao = 10

while opcao != 0:
    total = total + opcao
    while contador <= total:
        print(f'{pa}', end=' -> ')
        pa = pa + razao
        contador += 1
    print('PAUSA!')
    opcao = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados!')
print('FIM!')
