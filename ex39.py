'''ALISTAMENTO MILITAR'''

nascimento = int(input('Ano do seu nascimento: '))
ano_atual = int(input('Em que ano estamos: '))
idade = ano_atual - nascimento
diferença = 18 - idade
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')

if idade < 18:
    print(f'Ainda falta {diferença} anos para o alistamento')
    print(f'Seu alistamento será em {ano_atual + diferença}')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {ano_atual - (idade - 18)}')
else:
     print(f'Você tem que se alistar IMEDIATAMENTE')