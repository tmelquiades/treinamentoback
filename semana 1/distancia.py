# pergunte a distancia em km. calcule o preço da passagem cobrando R$1,50 por km
# para viagens de até 200km e R$1,25 por km para viagens mais longas

distancia = float(input('Informe a distância em quilômetros: '))

if distancia<=200:
    preco=distancia*1.5
else:
    preco=distancia*1.25

print('O valor da passagem é R${}' .format(preco))