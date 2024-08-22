media1 = 0
media2 = 0
maior1 = 0
maior2 = 0
velho = 0
nome = 0
masculino = 0
menores = 0
for x in range(1 , 3):
    print('-' * 20 , f'{x} pessoa' , '-' * 20)
    nome = str(input('Nome: '))
    idade = float(input('idade: '))
    sexo = input('sexo M/F: ') 
    if idade < 20:
        menores = menores + 1
    if sexo in 'Mm':
        masculino = masculino + 1
    if x == 1:
        media1 = idade
    if x == 2:
        media2 = idade
    if x == 1:
        maior1 = idade
        nome = nome
    if x == 2:
        maior2 = idade
        nome = nome
if maior1 > maior2:
    velho = maior1
    nome = nome
else:
    velho = maior2
    nome = nome
    
print(f'A média de idade do grupo é de {(media1 + media2) / 2:.2f} anos')
print(f'O homem mais velho tem {velho} anos e se chama {nome}')
print(f'Ao todo são {masculino} homens e também {menores} menores de 20 anos')
