def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return print(f'Com {idade} anos o voto é: NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos o voto é: OPCIONAL')
    else:
        return print(f'Com {idade} anos o voto é: OBRIGATÓRIO')


anoNascimento = int(input('Em que ano você nasceu? '))
voto(anoNascimento)
