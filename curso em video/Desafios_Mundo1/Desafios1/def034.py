sal = float(input('Qual é seu salário atual? '))
if sal > 1250:
    a1 = (sal * 10) / 100
    print('Seu novo salário será de R$ {:.2f}'.format(sal + a1))
else:
    a2 = (sal * 15) / 100
    print('Seu novo salário será de R$ {:.2f}'.format(sal + a2))
