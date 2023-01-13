print('-'*50)
print('LOJA TEM O QUE QUISER')
print('-'*50)
cont = total_gasto = maior_mil = mais_barato = valor = 0
produto = ''
while True:
    nome_produto = str(input('Digite o produto: ')).upper()
    preco = float(input('Qual valor R$ '))
    total_gasto += preco
    cont += 1
    if preco > 1000:
        maior_mil += 1

    if cont == 1: #simplifica com or preco < menor elimina o else
        mais_barato = preco
        produto = nome_produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            produto = nome_produto
            valor = preco

    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opcao == 'N':
        break

print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total gasto foi R$ {total_gasto:.2f},\nTemos {maior_mil} produtos custando mais de R$ 1000.00')
print(f'E o produto mais barato foi {produto} que custou R$ {valor:.2f}.')
