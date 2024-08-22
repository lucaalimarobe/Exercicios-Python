print(''' Jogo Pedra Papel e Tesoura''')

from random import randint
from time import sleep
itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
computador = randint(0 , 2)
nome = input('Qual é o seu nome? ')
print('''Escolha uma das opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!!')
sleep(1)
print('-' * 20)
print(f'Computador jogou {itens[computador]}')
print(f'{nome} jogou {itens[jogador]}')
print('-' * 20)
if computador == 0:
    if jogador == 0:
        print('DEU EMPATE')
    elif jogador == 1:
        print(f'{nome} GANHOU' )
    elif jogador == 3:
        print(f'Computador GANHOU')
elif computador == 1:
    if jogador == 0:
        print('Computador GANHOU')
    elif jogador == 1:
        print(f'DEU EMPATE')
    elif jogador == 2:
        print(f'{nome} GANHOU')
elif computador == 2:
    if jogador == 0:
        print (f'{nome} GANHOU')
    elif jogador == 1:
        print('computador GANHOU')
    elif jogador == 2:
        print('DEU EMPATE')