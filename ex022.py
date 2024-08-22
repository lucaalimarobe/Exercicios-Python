'''Analisador de Textos'''

nome = input('Digite seu nome completo: ')
nome_sem_espaços = nome.replace(' ', '')
primeiro_nome = nome.split()
print('Analisando seu nome... ')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome_sem_espaços)} letras')
print(f'Seu primeiro Nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras')