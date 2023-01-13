opcao = ''
num = media = cont = 0
maior = menor = 0
while opcao in 'Ss':
    num = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    media += num
    cont += 1

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num< menor:
            menor = num

media = media / cont
print('Foram digitados {} números, e a média dos valores é {}.'.format(cont, media))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
