import random
print('Vou sortear alguem para apagar a lousa. Digitem seus nomes para o sorteio!')
p1=input('Participante 1: ')
p2=input('Participante 2: ')
p3=input('Participante 3: ')
p4=input('Participante 4: ')
print('{}, {}, {} e {}, boa sorte!'.format(p1, p2, p3, p4))
sor=random.choice([p1, p2, p3, p4])
print('O sortudo é {} !'.format(sor))
