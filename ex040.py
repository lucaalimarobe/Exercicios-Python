''' Média do aluno'''

nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é de {media}')
if media < 5:
    print('Você está REPROVADO')
elif media <= 6.9:
    print('Você está de RECUPERAÇÃO')
else:
    print('Você está APROVADO')