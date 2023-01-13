vel = int(input('Digite a velocidade do seu carro: '))
val = (vel - 80) * 7
if vel >80:
    print('Multado! Ultrapassou a velocidade permitida de 80km/h.')
    print('Multa no valor de R$ {:.2f}'.format(val))
else:
    print('Muito bem, esta dentro da velocidade permitida!')
print('Boa viajem! dirija com segurança!')