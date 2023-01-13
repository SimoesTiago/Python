print('*** ANALISADOR COMPLETO ***')
soma_idade = 0
media_idade = 0
homem_mais_velho = 0
nome_velho = 0
total_mulheres_20 = 0
for c in range(1, 5):
    print('---- {}ª Pessoa ----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        homem_mais_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres_20 += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {}'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(homem_mais_velho, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(total_mulheres_20))
