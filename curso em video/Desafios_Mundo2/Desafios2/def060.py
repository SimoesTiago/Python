import math
n = ''
while n != 0:
    n = int(input('Digite um número inteiro: '))
    if n > 0:
        print('O fatorial de {}! é igual a {}'.format(n, math.factorial(n)))
if n == 0:
    print('Valor inválido! Fim do programa.')

# Com 'for' :
'''n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    f = f * c
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)'''

# Como era pra ser:

'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
