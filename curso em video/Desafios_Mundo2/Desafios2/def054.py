import datetime
contmaior = 0
contmenor = 0
atual= datetime.date.today().year
for c in range(1,8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
print('Ao todo temos {} pessoas maiores de idade'.format(contmaior))
print('E também temos {} pessoas menores de idade'.format(contmenor))
