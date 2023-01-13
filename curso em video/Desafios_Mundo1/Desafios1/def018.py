from math import sin, cos, tan, radians
ang=int(input('Digite o angulo desejado: '))
sen=sin(radians(ang))
cos=cos(radians(ang))
tan=tan(radians(ang))
print('Para o angulo de {}, temos o seno igual a {:.2f}.'.format(ang, sen))
print('Seu cosseno igual a {:.2f}, e sua tangente igual a {:.2f} .'.format(cos, tan))
