import random
import time
print('*'*10, '\033[7:30:47mJOGO DE JOKENPÔ\033[m', '*'*10)
escolha = input('''\033[32mJokeeeeeenpôô!\033[m Digite sua escolha:
(pedra, papel ou tesoura): ''').upper()
print('-'*20)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
time.sleep(1)
jkp = random.choice(lista)
if escolha == 'PAPEL' and jkp == 'PEDRA':
    print('Parabéns, {} ganha de {}'.format(escolha, jkp))
elif escolha == 'PAPEL' and jkp == 'TESOURA':
    print('Perdeu! {} ganha de {}.'.format(jkp, escolha))
elif escolha == 'PEDRA' and jkp == 'PAPEL':
    print('Perdeu! {} ganha de {}.'.format(jkp, escolha))
elif escolha == 'PEDRA' and jkp == 'TESOURA':
    print('Ganhou!!! {} vence {}.'.format(escolha, jkp))
elif escolha == 'TESOURA' and jkp == 'PAPEL':
    print('Parabéns!!! {} vence {}.'.format(escolha, jkp))
elif escolha == 'TESOURA' and jkp == 'PEDRA':
    print('Perdeu! {} vence a {}.'.format(jkp, escolha))
else:
    print('Empatamos! Escolhi {} e você {}.'.format(escolha, jkp))

#print(jkp)