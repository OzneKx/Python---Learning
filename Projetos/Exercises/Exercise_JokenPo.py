from random import randint
from time import sleep
print('VAMOS JOGAR JOKENPÔ? ')
listaEscolhas = ('PEDRA', 'PAPEL', 'TESOURA')
escolhaComputador = randint(0, 2)
print('Escolhas possíveis \n'
    '[0] PEDRA\n'
    '[1] PAPEL\n'
    '[2] TESOURA')
suaEscolhaAgora = int(input('Digite sua escolha: '))
print('\033[33m=-='*10)
print('{:=^}'.format('\033[33mVocê escolheu\033[m ''\033[7;30m''{}''\033[m').format(listaEscolhas[suaEscolhaAgora]))
print('{:=^}'.format('\033[33mO computador escolheu\033[m ''\033[7;30m''{}''\033[m').format(listaEscolhas[escolhaComputador]))
print('\033[36m=-='*10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('=-=' * 10)
if escolhaComputador == 0: #COMPUTADOR JOGOU PEDRA
    if suaEscolhaAgora == 0:
        print('\033[36mEMPATE!\033[m')
    elif suaEscolhaAgora == 1:
        print('Você \033[32mGANHOU!\033[m')
    elif suaEscolhaAgora == 2:
        print('Você \033[31mPERDEU!\033[m')
    elif suaEscolhaAgora > 2:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif escolhaComputador == 1: #COMPUTADOR JOGOU PAPEL
    if suaEscolhaAgora == 0:
        print('Você \033[31mPERDEU!\033[m')
    elif suaEscolhaAgora == 1:
        print('\033[36mEMPATE!\033[m')
    elif suaEscolhaAgora == 2:
        print('Você \033[32mGANHOU!\033[m')
    elif suaEscolhaAgora > 2:
        print('\033[31mJOGADA INVÁLIDA!\033[m')
elif escolhaComputador == 2: #JOGADOR JOGOU TESOURA
    if suaEscolhaAgora == 0:
        print('Você \033[32mGANHOU!\033[m')
    elif suaEscolhaAgora == 1:
        print('Você \033[31mPERDEU!\033[m')
    elif suaEscolhaAgora == 2:
        print('\033[36mEMPATE!\033[m')
    elif suaEscolhaAgora > 2:
        print('\033[31mJOGADA INVÁLIDA!\033[m')