print('-=-'*4, 'TABUADA', '-=-'*4)
num = int(input('Digite um número inteiro: '))
for c in range(1, 11, 1):
    print('{} x {:2} = {}'.format(num, c, num * c))
print('-=-'*10)
