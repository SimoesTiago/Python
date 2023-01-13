print(' --- Gerador de PA ---')
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
termo2=termo3=termo4 = 0
while termo != 0:
    termo2= termo + razao
    termo3= termo2 + razao
    termo4= termo3 + razao
    termo5= termo4 + razao
    pa=(termo, termo2, termo3, termo4)
    print(pa)
    break