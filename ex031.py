distancia = float(input('Qual é a distancia da sua viagem? '))

if distancia <= 200:
    print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km')
    print(f'E o preço da sua passagem será de R${distancia * 0.50:.2f}')
else:
    print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km')
    print(f'E o preço da sua passagem será de R${distancia * 0.45:.2f}')