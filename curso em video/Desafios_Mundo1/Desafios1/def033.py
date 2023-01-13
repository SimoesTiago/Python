num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3
maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))
