'''Sorteando em ordem '''
import random

n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
s1 = [n1 , n2 , n3 , n4]
random.shuffle(s1)

print(f'a ordem de apresentação será {s1}')