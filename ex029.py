velocidade = int(input('Qual é a velocidade do veiculo? '))
multa = float((velocidade - 80) * 7.00)

if velocidade > 80:
    print('MULTADO!!! Você excedeu o limite permitido que é de 80km/h ')
    print(f'Você deve pagar uma multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com cuidado.')