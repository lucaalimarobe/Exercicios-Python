''' Calcular o IMC '''

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / altura**2
print(f'O IMC dessa pessoa é de {imc:.2F}')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25: 
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBSIDADE MÓRBIDA')