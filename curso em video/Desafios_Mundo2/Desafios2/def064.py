s = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Digite um número [999 para PARAR]: '))
    if num != 999:
        s += num
        cont += 1
if num == 999:
    print('Fim')
print('Foram {} números digitados, a soma entre eles é igual a {}'.format(cont, s))
