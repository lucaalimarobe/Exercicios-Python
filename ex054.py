from datetime import date
data_atual = date.today().year
soma = 0
totalmaior = 0
totalmenor = 0
for x in range(1, 3):
    ano = int(input(f'Em que ano a {x}a pessoa nasceu? '))
    soma = soma + 1
    idade = data_atual - ano
    if idade < 18:
        totalmenor = totalmenor + 1
    else:
        totalmaior = totalmaior + 1
print(f'Ao todo tivemos {totalmaior} pessoas maiores de idade')
print(f'E também tivemos {totalmenor} pessoas menores de idade')