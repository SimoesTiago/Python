from random import randint
from time import sleep
computador = randint(0, 10)
print('\033[31mComputador\033[m: Vou pensar em um número entre 0 a 10, tente adivinhar...')
sleep(1)
print('... \033[1:32mProcessando\033[m...')
sleep(2)
jogador = ''
total_jogadas = 0
while jogador != computador:
    jogador = int(input('Qual seu palpite? '))
    total_jogadas += 1
    if jogador == computador:
        print('\033[1:32mParabéns!\033[m Você precisou de {} palpites para me vencer.'.format(total_jogadas))
    else:
        if jogador < computador:
            print('\033[34mMais... \033[33mTente novamente\033[m')
        elif jogador > computador:
            print('\033[36mMenos... \033[33mTente novamente\033[m')

