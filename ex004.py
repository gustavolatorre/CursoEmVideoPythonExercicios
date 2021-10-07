var = input('Digite algo: ')
print(f'''O tipo primitivo desse valor é {type(var)}
Só tem espaços? {var.isspace()}
É um número? {var.isnumeric()}
É Alfabético? {var.isalpha()}
É alfanumérico? {var.isalnum()}
Está em maiúsculas {var.isupper()}
Esté em minúsculas? {var.islower()}
Está capitalizado? {var.istitle()}''')