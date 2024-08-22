'''Pintando Parade'''

largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))

area = largura*altura

print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area:.3f}m²')
print(f'Para pintar essa parede, você precisará de {area / 2}l de tinta')