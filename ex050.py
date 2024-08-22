soma = 0
for x in range(1 , 7):
    x = int(input('Digite qualquer número: '))
    if x % 2 == 0:
        soma = soma + x
        
print(f' a soma dos numeros pares é {soma}')