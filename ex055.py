maior = 0
menor = 0
for x in range(1 , 4):
    peso = float(input(f'Peso da {x}a pessoa:  '))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O peso MAIOR é de {maior} ')
print(f'O peso menor é de {menor}')