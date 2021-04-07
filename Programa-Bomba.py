#Programa Bomba#

import time

contagem = 11

while contagem > 0:
    contagem = contagem - 1
    time.sleep (0.8)
    print(contagem)

    if contagem == 0:
        print('A BOMBA EXPLODIU!!!')

