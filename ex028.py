'''Jogo da Adivinhação'''
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou Pensar em um número de 0 até 5. Tente Adivinhar!!')
print('-=-' * 20)

computador = randint(0 , 5)
n1 = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if n1 == computador:
    print('PARABÉNS ! Você Conseguiu me Vencer!!')
else:
    print(F'GANHEI ! Pensei no número {computador} e não no {n1}')
