while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO.')
