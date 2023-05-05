# faça um programa que leia 3 números inteiros e informe se estes são iguais ou diferentes, mostrando uma das mensagens: "Três iguais" OU "Dois iguais" OU "Três diferentes";

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))

if num1==num2 and num2==num3:
  print('Três iguais')
elif num1==num2 or num1==num3 or num2==num3:
  print('Dois iguais')
else:
  print('Três diferentes')