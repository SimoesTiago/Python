from time import sleep
from random import randint
import emoji
print('-' * 30)
print('-=-'*3, '\033[7:40mjO\033[m''_''KeN''_''\033[7:40mPôÔ\033[m', '-=-'*3)
print('-' * 30)
itens = [(emoji.emojize(':oncoming_fist:')), (emoji.emojize(':raised_hand:')), (emoji.emojize(':scissors:'))]
computador = randint(0, 2)
while True:
    print('''Suas opções:

    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA

    [999] sair''')
    print()
    jogador = int(input('Sua jogada => '))
    if jogador == 999:
        break
    print('\033[7:40mJO\033[m')
    sleep(1)
    print('KEN')
    sleep(1)
    print('\033[7:40mPÔ\033[m!!!')
    sleep(1)
    print('-=-'*11)
    print('O computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=-'*11)
    if computador == 0:
        if jogador == 0:
            print('\033[33mEMPATE\033[m')
        elif jogador == 1:
            print('\033[32mJOGADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 1:
        if jogador == 0:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        elif jogador == 1:
            print('\033[33mEMPATE\033[m')
        elif jogador == 2:
            print('\033[32mJOGADOR VENCE\033[m')
        else:
            print('JOGADA INVÁLIDA!')
    elif computador == 2:
        if jogador == 0:
            print('\033[32mJOGADOR VENCE\033[m')
        elif jogador == 1:
            print('\033[31mCOMPUTADOR VENCE\033[m')
        elif jogador == 2:
            print('\033[33mEMPATE\033[m')
        else:
            print('JOGADA INVÁLIDA!')
