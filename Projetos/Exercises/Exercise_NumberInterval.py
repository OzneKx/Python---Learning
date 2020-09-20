numeros0_25 = 0
numeros26_50 = 0
numeros51_75 = 0
numeros76_100 = 0
contad0r = 1
qualNumero = 1
while qualNumero > 0:
    qualNumero = int(input('Digite um número entre 0 a 100: '))
    if qualNumero > 0:
        contad0r += 1
        if 0 <= qualNumero <= 25:
            numeros26_50 +=1
        elif 25 < qualNumero <= 50:
            numeros51_75 += 1
        elif 51 < qualNumero <= 75:
            numeros51_75 += 1
        else:
            numeros76_100 += 1
    else: continue
print('No intervalo de 0 a 25, existem {} números. '.format(numeros0_25))
print('No intervalo de 26 a 50, existem {} números. '.format(numeros26_50))
print('No intervalo de 51 a 75, existem {} números. '.format(numeros51_75))
print('No intervalo de 76 a 100, existem {} números. '.format(numeros76_100))