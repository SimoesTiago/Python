prod=int(input('O valor deste produto é R$ '))
desc=(prod*5/100)
print('Mas com o desconto de 5%, fica por R$ {:.2f} !'.format(prod-desc))
