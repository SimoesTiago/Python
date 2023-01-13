ano = float(input('Digite um ano qualquer: '))
res = ano % 4
if res ==0:
    c1 = ano % 100
    if c1 !=0:
        print('O ano de {:.0f} é BISSEXTO!'.format(ano))
else:
    print('O ano de {:.0f} não é BISSEXTO!'.format(ano))
