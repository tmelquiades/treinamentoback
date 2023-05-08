#faça um programa que capture uma frase e conte o número de caracteres de uma frase, não levando
#em consideração os espaços à direita e/ou à esquerda. Mostrar a frase e a quantidade encontrada;

frase = str(input('Digite uma frase: '))

print(frase)
print('Quantidade de caracteres:', len(frase.strip(' '))) #caracteres da frase