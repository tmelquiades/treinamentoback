salario = float(input('Informe o valor do salário recebido: '))
gastos = float(input('Informe o valor dos gastos: '))
if gastos > salario:
  print('Gastos fora do orçamento')
else:
  print('Gastos dentro do orçamento')