tabuadaNumeroQualquer = int(input('Digite um número qualquer, vamos ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tabuadaNumeroQualquer, c, tabuadaNumeroQualquer * c))