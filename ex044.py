'''Gerenciador de Pagamentos'''

print('============ IMPORTS LUCAS ============')

valor = float(input('Digite o preço das compras: '))

print('FORMAS DE PAGAMENTO')
print('[1] a vista dinheiro / cheque')
print('[2] à vista Cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

escolha = int(input('Qual a opção? '))
if escolha == 1:
    print(f'sua compra de {valor:.2f}, vai custar { valor - (valor * 0.10):.2f} com 10% de desconto')
elif escolha == 2:
    print(f'sua compra de {valor:.2f}, vai custar {valor - (valor * 0.05):.2f} com 5% de desconto')
elif escolha == 3:
    print(f'sua compra de {valor:.2f}, vai custar 2x de {valor / 2} ')
elif escolha == 4:
    print(f'sua compra de {valor:.2f}, vai custar {valor + (valor * 0.20):.2f} com aumento de 20% de juros')