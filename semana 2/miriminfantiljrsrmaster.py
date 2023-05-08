#A confederação Nacional de Futsal precisa de um programa
#que leia o ano de nascimento de um atleta e mostre sua categoria,
#de acordo com a idade:
#- até 9 anos: MIRIM
#- até 14 anos: INFANTIL
#- até 19 anos: JUNIOR
#- até 20 anos: SÊNIOR 
#- acima: MASTER

nasc = int(input('Digite o ano de nascimento: '))
idade = 2023-nasc

if idade <= 9 :
  print('MIRIM')
elif idade > 9 and idade <= 14:
  print('INFANTIL')
elif idade > 14 and idade < 19:
  print('JUNIOR')
elif idade == 19 or idade == 20:
  print('SENIOR')
else:
  print('MASTER')