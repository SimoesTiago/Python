# n = soma dos dois antecessores
# 0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
print('~~~~~~ Sequencia de Fibonacci ~~~~~~')
num = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' Fim')