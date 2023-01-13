print('*'*10, 'PROGRESSÃO ARITMÉTICA', '*'*10)
t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(t1, r*10+t1, r):
    print(c, end=' ')
print('FIM')
