import random
print('Atenção para a ordem da apresentação do trabalho, digitem seus nomes para o sorteio:')
a1= input('Aluno 1: ')
a2= input('Aluno 2: ')
a3= input('Aluno 3: ')
a4= input('Aluno 4: ')
print('Muito bem, {}, {}, {} e {}. Boa sorte!'.format(a1, a2, a3, a4))
lista=[a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem conforme sorteio é:\n{}.'.format(lista))
