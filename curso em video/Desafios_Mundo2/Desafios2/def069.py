print('-'*5, 'CADASTRO DE PESSOAS', '-'*5)
print('-'*30)
total_pessoas = maior_idade = sexo_m = fem_menor = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    total_pessoas += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M':
        sexo_m += 1
    if sexo == 'F':
        if idade < 20:
            fem_menor += 1
    opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    print('-'*30)
    if opcao == 'N':
        break
print('-=-'*10)
print(f'''FORAM CADASTRADOS TOTAL DE {total_pessoas} PESSOAS:
 {maior_idade} pessoas maiores de 18 anos.\n {sexo_m} Homens \n {fem_menor} Mulheres com menos de 20 anos.''')
