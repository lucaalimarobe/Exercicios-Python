soma = 0
cont = 0
for x in range(1 , 501, 2):
    if x % 3 == 0:
        cont = cont + 1
        soma = soma + x
print(f"A soma {cont} dos múltiplos de 3 do 1 a 500 é: {soma}")