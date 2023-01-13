print('-'*10, 'APROVANDO EMPRÉSTIMOS', '-'*10)
casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é seu salário? R$ '))
anos = int(input('Em quantos anos? '))#divir em meses
parcelas = anos * 12 #Qtdd de parcelas
prestacao = casa / parcelas #valor mensal
sal1 = (salario * 30) / 100 #30% do salario
if prestacao <= sal1:
    print('Sua prestação será de R$ {:.2f} .'.format(prestacao))
    print('\033[1:32mVamos te conceder o EMPRÉSTIMO!!!\033[m')
else:
    print('\033[31mInfelizmente NÃO podemos te conceder o empréstimo\033[m.')
