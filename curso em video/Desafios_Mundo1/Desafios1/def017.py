from math import hypot
print('> '*5 + ('Calculando a Hipotenusa de um triangulo retangulo') + ' <'*5)
n1=float(input('Digite o valor do cateto oposto: '))
n2=float(input('Digite o valor do cateto adjacente: '))
print('A hipotenusa do triângulo retangulo calculado equivale a {:.0f} !'.format(hypot (n1, n2)))
