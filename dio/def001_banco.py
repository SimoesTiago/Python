from datetime import date
from time import sleep

saldo = depositos = saques = 0
valor_saque = 500
lim_saque = 3
extratos = {}
extrato = list()

print(' \033[1mBANCO SIMON\033[m '.center(30, '='))
print('-' * 30)
print ('''Escolha a opção desejada:
    [1] SAQUE
    [2] DEPÓSITO
    [3] EXTRATO
    [4] SALDO

    [0] para SAIR''')
print('-' * 30)
while True:
    try:
        menu = int(input('\033[33mOpção Menu\033[m => '))
        if menu == 1:
            saque = float(input('Qual valor deseja sacar? R$ '))
            if saque > 0:
                if saque <= saldo:
                    if saques < lim_saque:
                        if saque <= valor_saque:
                            print('Processando...')
                            sleep(1)
                            print('>> Retire suas notas..')
                            sleep(0.5)
                            print(' > Saque realizado com sucesso!')
                            extratos.clear()
                            saldo = saldo - saque
                            saques += 1
                            extratos['saque_(-)R$'] = (f'{saque:.2f}')
                            extrato.append(extratos.copy())

                        else:
                            sleep(1)
                            print(f'!> Seu limite de saque é R$ {valor_saque:.2f} por operação.')        
                    else:
                        sleep(1)
                        print(f'!> Limite de saque atingido, foram efetuados {saques}/{lim_saque} saques.')
                else:
                    sleep(1)
                    print(f'!> Saldo insuficiente! Seu saldo é de R$ {saldo:.2f}.')
            else:
                print('!> Para efetuar um saque, insira um valor válido!')
        elif menu == 2:
            deposito = float(input('Qual valor deseja depositar? R$ '))
            if deposito > 0:
                extratos.clear()
                saldo = saldo + deposito
                depositos += 1
                extratos['deposito R$'] = (f'{deposito:.2f}')
                extrato.append(extratos.copy())
                sleep(1)
                print('>> Processando...')
                sleep(1)
                print(' > Deposito efetuado com sucesso.')
            else:
                print('!> Para depositar, insira um valor válido!')
        
        elif menu == 3:
            if len(extrato) == 0:
                print('!> Não existe movimentações para exibir.')
                print(f'>>> Seu saldo é de R$ {saldo:.2f}')
            else:
                print()
                print('Banco Simon'.center(30, '*').upper())
                print('Extrato'.center(30, '='))
                print(f'Data .............. {date.today()}')
                print('-' * 30)
                for i, v in enumerate(extrato):
                    print(f'{i+1:<3}', end='')
                    for k, v in v.items():
                        print(f'{k:<10}  {v:>10}')
                print('=' * 30)
                print(f'Saldo atual R$ {saldo:>10.2f}')
                print('=' * 30)
                print()

        elif menu == 4:
            print(f'>>> Seu saldo é de R$ {saldo:.2f}')
        
        elif menu == 0:
            break
        else:
            print('!> Opção inválida. Tente novamente.')
    except ValueError:
        print('!!!ERRoR > Essa não é uma opção válida! Tente novamente. <<')
        