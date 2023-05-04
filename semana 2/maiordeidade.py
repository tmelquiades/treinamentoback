nascimento = int(input('Qual seu ano de nascimento? '))
idade = 2023 - nascimento
if idade>=18:
  print('Maior de idade. A idade é {}' .format(idade))
else:
  print('Menor de idade. A idade é {}' .format(idade))