'''menor e maior numero'''

v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo Valor: '))
v3 = int(input('Terceiro Valor: '))
 
menor = v1
if v2 < v1:
    menor = v2
if v3 < v2:
    menor = v3
print(f'O menor valor é {menor}')

maior = v1
if v2 > v1:
    maior = v2
if v3 > v2:
    maior = v3
print(f'O maior valor é {maior}')