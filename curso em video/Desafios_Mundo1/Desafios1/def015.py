dias=int(input('Quantos dias alugado? '))
km=float(input('Quantos KM foram rodados? '))
valor=dias * 60 + km * 0.15
print('O valor total do aluguel do carro ficou R$ {:.2f}.'.format(valor))
