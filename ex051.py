print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + 10 * razao
for x in range(termo , decimo, razao):
    print(f'{x} ' , end = '-> ')
print('ACABOU') 