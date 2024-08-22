num = int(input('Digite uma número: '))
divisivel = 0
for x in range(1 , num + 1):
    if num % x == 0:
        print(f'\033[32m{x}' , end=' ')
        divisivel = divisivel + 1
    else:
        print(f'\033[31m{x}' , end=' ')
print(f'\n\033[37mO número {num} foi divisivel {divisivel} vezes')
if divisivel == 2:
    print(f'\033[37mE por isso É PRIMO')
else:
    print('\033[37mE por isso NÃO É PRIMO')