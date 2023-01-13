'''sexo = 1
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo [M / F]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Valor inválido, tente novamente.')
print('Sexo {}, obrigado!'.format(sexo))'''

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido! Informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))
