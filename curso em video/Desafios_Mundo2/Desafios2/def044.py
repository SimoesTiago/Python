import time
print('='*10, '/// \033[4:31mGERENCIADOR DE PAGAMENTOS\033[m ///', '='*10)
prod = float(input('Digite o valor do produto: R$ '))
print('Qual será a forma de pagamento? Temos as formas a abaixo:')
formas = ['à vista ou cheque 10% de desconto', 'à vista no cartão 5% de desconto', 'Em até 2x no cartão sem juros', 'Em 3x ou mais no cartão 20% de juros']
print(' '*10, '\033[34mDigite "0" para à vista ou cheque tem 10% de desconto.')
print(' '*10, '\033[34mDigite "1" para à vista no cartão tem 5% de desconto.')
print(' '*10, '\033[34mDigite "2" para em até 2x no cartão é sem juros.')
print(' '*10, '\033[34mDigite "3" para 3x ou mais no cartão tem juros de 20%.\033[m')
forma = int(input('Digite a forma de pagamento escolhida: '))
print('='*30, 'Processando...')
time.sleep(2)
opcao = formas[forma]
print(' '*5, opcao)
if forma == 0:
    print('\033[32mSeu produto de R$ {:.2f}, ficará por R$ {:.2f}.\033[m'.format(prod, prod - (prod*10)/100))
elif forma == 1:
    print('\033[33mSeu produto de R$ {:.2f}, fica por R$ {:.2f}.\033[m'.format(prod, prod - (prod*5)/100))
elif forma == 2:
    print('\033[35mSeu produto de R$ {:.2f},fica 2 parcelas de R$ {:.2f}.\033[m'.format(prod, prod/2))
else:
    vezes = int(input('\033[7:30:41mEm quantas vezes deseja dividir?\033[m '))
    condicao = (prod * 20) / 100 + prod
    print('\033[36mSeu produto fica por R$ {:.2f}, em {} parcelas de R$ {:.2f}.\033[m'.format(prod+(prod*20)/100, vezes, condicao / vezes))
print(' ')
print('\033[1:32mObrigado pela preferência!!!\033[m')
