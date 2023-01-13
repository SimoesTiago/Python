a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas digitadas PODEM formar um triângulo.')
else:
    print('As retas digitadas NÃO podem formar um triângulo.')
