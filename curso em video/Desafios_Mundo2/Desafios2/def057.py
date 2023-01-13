sexo = 1
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo: ').strip().upper()[0])
    if sexo != 'F' and sexo != 'M':
        print('Valor incorreto! Tente novamente!')
print('{}, Obrigado!'.format(sexo))
