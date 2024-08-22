'''aumento multiplos'''

salario = float(input('Qual o salário do funcionario? '))

if salario > 1250:
    aumento = salario * 0.10 + salario
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')
else:
    aumento = salario * 0.15 + salario
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')