#Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:
#- média abaixo de 5.0: REPROVADO
#- média entre 5.0 a 6.9: RECUPERAÇÃO
#- média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if (n1+n2)/2 >=7 and (n1+n2)/2 <=10 :
  print('APROVADO')
elif (n1+n2)/2 >= 5 and (n1+n2)/2 < 7:
  print('RECUPERAÇÃO')
elif (n1+n2)/2 < 5 and (n1+n2)/2 > 0:
  print('REPROVADO')
else:
  print('Digite valores válidos')