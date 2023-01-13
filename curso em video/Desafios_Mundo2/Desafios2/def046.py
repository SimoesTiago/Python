from time import sleep
import emoji
print('Contagem regressima para os fogos de artifício!')
for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print('BUM!!! POOOW!!!', emoji.emojize(':fireworks::sparkler::fireworks::sparkler:'))
