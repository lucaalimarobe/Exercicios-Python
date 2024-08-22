'''Aprovando Empréstimo'''

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcela = casa / (anos * 12)
maximo = 0.30*salario

print(f'Para pagar uma casa de {casa:.2f} em {anos} a prestação será de R${parcela:.2f}')

if parcela > maximo:
    print('EMPRESTIMO NEGADO')

else:
    print('EMPRESTIMO ACEITO')