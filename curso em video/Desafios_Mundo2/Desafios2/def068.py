from random import randint
from time import sleep
print('-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*10)
cont = 0
while True: #Faltou tratar escolha != P ou I pra perguntar novamente.
    valor_computador = randint(0, 10)
    valor_jogador = int(input('Diga um valor: '))
    escolha = ' '# aqui
    while escolha not in 'PI': # aqui
        escolha = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    jogada = valor_jogador + valor_computador
    resultado = jogada
    print('-'*30)
    if resultado % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'Você jogou {valor_jogador} e o computador {valor_computador}. Total de {jogada} que é {resultado}')
    print('-'*30)
    sleep(1.5)
    if resultado[0] == escolha:
        print('\033[1:32mVocê VENDEU!\033[m')
        print('Vamos jogar novamente...')
        cont += 1
        print('-' * 30)
    else:
        print('Você PERDEU!')
        break
print('-=-'*20)
print(f'\033[1:31mGAME OVER!!!\033[m Você venceu {cont} vezes.')
