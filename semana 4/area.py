def area(larg,comp):
    a = larg*comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')

def linhas():
    print('-'*40)

linhas()
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
linhas()
area(l,c)
linhas()