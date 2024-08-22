'''Aluguel de carros'''

dias = float(input('Quantos dias Alugados: '))
km = float(input('Quantos Km rodados? '))

print(f'Total a pagar é de R${(dias * 60) + (km * 0.15):.2f}')