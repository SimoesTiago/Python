print('-=-'*5, 'CALULADORA DE IMC', '-=-'*5)
print('-'*50)
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura separado por "."(m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('IMC {:.2f} - \033[36mABAIXO DO PESO\033[m!!!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC {:.2f} - \033[32mPESO IDEAL\033[m!!!'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC {:.2f} - \033[33mSOBREPESO\033[m!!!'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC {:.2f} - \033[35mOBESIDADE\033[m!!!'.format(imc))
else:
    print('IMC {:.2f} - \033[31mOBESIDADE MÓRBIDA\033[m!!!'.format(imc))
print('='*50)
