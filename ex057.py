sexo = str(input('Informe seu sexo: [M/F]: '))
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos, por favor!! Digite novamente: '))
print('sexo {} registrdo com sucesso'.format(sexo))
