#faça um programa que mude uma palavra da String "treinamento hoje de backend", capturando do teclado duas palavras: a que deverá ser trocada por qual palavra;

frase = 'treinamento hoje de backend'

palavra1 = str(input('Digite a palavra que deverá ser trocada: '))
palavra2 = str(input('Digite a palavra que irá substituir: '))

print(frase.replace(palavra1, palavra2))