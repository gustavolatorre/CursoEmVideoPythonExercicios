times = ('Atlético Mineiro', 'Fortaleza', 'Flamengo', 'Palmeiras', 'Bragantino', 'Internacional', 'Corinthians',
         'Fluminense', 'América MG', 'Cuiabá', 'Athletico PR', 'Atlético Goianiense', 'São Paulo', 'Ceará', 'Bahia',
         'Juventude', 'Santos', 'Sport Recife', 'Grêmio', 'Chapecoense')

print(f'''Lista de times do Brsileirão: {times}
Os 5 primeiros são: {times[:5]}
Os quatro últimos são: {times[-4: ]}
Times em ordem alfabética: {sorted(times)}
O Chapecoense está na {times.index('Chapecoense')+1} posição''')
