print('#'*5, 'ANALISADOR DE TRIÂNGULOS', '#'*5)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Forma um triângulo:')
if r1 == r2 and r2 == r3 and r3 == r1:
    print('\033[32mEquilátero')
elif r1 == r2 or r2 == r3:
    print('\033[33mIsósceles')
elif r1 != r2 and r2 != r3 and r3 != r1:
    print('\033[34mEscaleno')
else:
    print('Não forma um triângulo')
