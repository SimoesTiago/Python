import random
print('--- ADIVINHE O NÚMERO ---')
print('??? Pensei em um número de 0 e 5!')
lista= [0 , 1, 2, 3, 4, 5]
n1 = int(input('Digite qual número pensei: '))
num = random.choice(lista)
if num == n1:
    print('Parabéns! Pensei {}, e digitou {}!'.format(num, n1))
else:
    print('Errou! Pensei {}, e digitou {}!'.format(num, n1))
print('--- FIM ---')
