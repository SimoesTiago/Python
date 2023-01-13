from datetime import date
print('--=--'*2, 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO', '--=--'*2)
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
lista = ['MIRIM', 'INFANTIL', 'JUNIOR', 'SÊNIOR', 'MASTER']
if idade <= 9:
    print('Você tem {} anos. Sua categoria é a {}.'.format(idade, lista[0]))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos. Sua categoria é a {}.'.format(idade, lista[1]))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos. Está na categoria {}.'.format(idade, lista[2]))
elif idade > 19 and idade == 20:
    print('Você tem {} anos. Sua categoria é {}.'.format(idade, lista[3]))
else:
    print('Você tem {} anos. Esta na categoria {}.'.format(idade, lista[4]))
print('\033[1:33mBORA NADAR\033[m!!!')
