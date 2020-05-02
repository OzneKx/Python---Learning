from random import randint
from time import sleep
from operator import itemgetter
dictJogoDado = {'Jogador 1': randint(1, 6),
                'Jogador 2': randint(1, 6),
               'Jogador 3': randint(1, 6),
               'Jogador 4': randint(1, 6)}
rankingJogoDado = []
for key, numeroDado in dictJogoDado.items():
    print(f'{key} tirou {numeroDado} no dado. ')
    sleep(0.5)
rankingJogoDado = sorted(dictJogoDado.items(), key=itemgetter(1), reverse=True)
for c, value in enumerate(rankingJogoDado):
    print(f'Em {c + 1}º lugar: {value[0]} com {value[1]}')
    sleep(0.5)