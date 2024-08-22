'''Conversor de bases númericas'''

num = int(input("Digite um número inteiro: "))

print("Escolha uma das opções:")
print("[1] Converter para Binário")
print("[2] Converter para Octal")
print("[3] Converter para Hexadecimal")

escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'{num} convertido em Binário é {bin(num) [2:]}')
elif escolha == 2:
    print(f'{num} convertido em Octal é {oct(num) [2:]}')
else:
    escolha == 3
    print(f'{num} convertido em hexadecimal é {hex(num) [2:]}')
    