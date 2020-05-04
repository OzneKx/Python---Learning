soma = totalNumeros = 0
while True:
    digiteUmNumeroAqui = int(input('Digite um número: '))
    if digiteUmNumeroAqui != 999:
        soma += digiteUmNumeroAqui
        totalNumeros += 1
    else:
        break
print('Foram mostrados {} números. A soma entre eles é igual a: {} '.format(totalNumeros, soma))