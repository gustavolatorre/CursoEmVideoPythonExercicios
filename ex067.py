num = 0
tabuada = 0

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('='*40)
    if num < 0:
        break
    for i in range(1, 11):
        tabuada = num * i
        print(f'{num} x {i:2} = {tabuada}')
    print('=' * 40)
print('Programa Tabuada Encerrado! Volte sempre!')