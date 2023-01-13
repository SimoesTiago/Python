print('*'*10, 'MÉDIA', '*'*10)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua media foi {}. Esta \033[1:31mREPROVADO\033[m!!! Estude mais!'.format(media))
elif media >= 5.0 and media < 6.9:
    print('''Sua média foi {}. Esta de \033[1:33mRECUPERAÇÃO\033[m!!!
    Diga adeus aos finais de semana!'''.format(media))
else:
    print('Sua média foi {}, está \033[1:32mAPROVADO\033[m!!!'.format(media))
    print('PARABÉNS!!!')
