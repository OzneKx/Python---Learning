numeroPrimo = int(input('Digite um número para se descobrir se ele é primo: '))
contagem = 0
for c in range(1, numeroPrimo+1):
    if numeroPrimo % c == 0:
        contagem += 1
if contagem == 2:
    print('O número é primo! ')
else:
    print('O número não é primo! ')
    for c in range(1, numeroPrimo + 1):
        if numeroPrimo % c == 0:
            print(c, end=' -> ')
        else: continue
    else:
        print('O número é divisivel por: {} portanto, não é primo'.format(numeroPrimo))