d = float(input('Digite uma distância em metros: '))
kilometro = d / 1000
hectometro = d /100
decametro = d / 10
decimetro = d * 10
centimetro = d * 100
milimitro = d * 1000

print(f'''A medida de {d}m corresponde a
{kilometro}km
{hectometro}hm
{decametro}dam
{decimetro}dm
{centimetro}cm
{milimitro}mm''')

