'''Desconto de 5%'''

produto = float(input('Qual o valor do produto? R$'))
desconto = produto * 0.05

print(f'O produto custava R${produto}, na promoção com desconto de 5% vai custar R${produto - desconto:.2f}.')