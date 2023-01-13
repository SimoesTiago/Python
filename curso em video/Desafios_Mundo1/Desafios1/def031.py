km = int(input('Qual a distância em km da sua viagem? '))
if km <= 200:
    km1 = km * 0.50
    print('Sua passagem custará {:.2f}'.format(km1))
else:
    km2 = km * 0.45
    print('Sua passagem custará {:.2f}'.format(km2))
print('Teha uma otima viagem!')
