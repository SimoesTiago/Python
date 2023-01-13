from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''Menu de opcões:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
Digite sua escolha: '''))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é igual a {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação entre {} e {} é igual a {}'.format(valor1, valor2, multiplicar))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        elif valor1 == valor2:
            maior = 'nenhum, são iguais'
        else:
            maior = valor2
        print('O maior número entre {} e {} é {}'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Reiniciando...')
        sleep(1)
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente.')
    print('-=-'*10)
    sleep(1.5)
print('Fim do programa! Volte sempre.')
