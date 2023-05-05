#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com sua idade:
#a. se ele ainda vai se alistar ao serviço militar
#b. se é a hora de se alistar.
#c. se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que passou do prazo

from datetime import date

atual = date.today().year
nasc = int(input('Informe o ano de nascimento: '))

if atual - nasc < 18:
  print('Ainda vai se alistar')
elif atual - nasc == 18:
  print('É hora de se alistar')
else:
  print('Já passou do tempo de alistamento. Você deveria ter ido há' ,atual - nasc - 18, 'anos')