from datetime import date
print('*'*10, 'ALISTAMENTO MILITAR', '*'*10)
ano = int(input('Em que ano nasceu? '))
idade = date.today().year - ano
resto = 18 - idade
resto1 = idade - 18
if idade < 18:
    print('Você tem {} anos, ainda vai se alistar no serviço militar.'.format(idade))
    print('Faltam {} anos. Fique atento!'.format(resto))
elif idade == 18:
    print('Você completou {} anos, é hora de se alistar no serviço militar!'.format(idade))
else:
    print('Você já passou do tempo para alistamento!'.format(idade))
    print('Já se passaram {} anos!'.format(resto1))
print('\033[1:31mBOA SORTE!!!\033[m')
