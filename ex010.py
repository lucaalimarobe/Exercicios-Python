'''Conversor de moedas'''

print('-'*50)

dinheiro = float(input('Quanto dinheiro você está na carteira? R$'))
conversor = dinheiro * 0.20

print(f'Com R${dinheiro} você pode comprar U${conversor:.2f}')

print('-'*50) 