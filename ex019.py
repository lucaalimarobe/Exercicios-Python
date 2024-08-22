'''Sorteando um item na lista '''
import random

n1 = input(f'Primeiro Aluno: ')
n2 = input(f'Segundo Aluno: ')
n3 = input(f'Terceiro Aluno: ')
n4 = input(f'Quarto Aluno: ')
sorteio = [n1 , n2 , n3 , n4]

sr1 = random.choice(sorteio)
print(f'O aluno escolhido foi {sr1}')