divida = float(input('Digite o valor da divida: '))
parcela = 1
print('Valor da dívida      Valor dos Juros         Quantidade de Parcelas      Valor da Parcela')
for i in range(5):
    if parcela == 1:
        juros = 1
        valor_juros = 0
    elif parcela == 4:
        parcela = 3
        juros = 1.10
    elif parcela == 7 or parcela == 6:
        parcela = 6
        juros = 1.15
    elif parcela == 10 or parcela == 9:
        parcela = 9
        juros = 1.20
    elif parcela == 13 or parcela == 12:
        parcela = 12
        juros = 1.25
    valorJuros = divida * (juros - 1)
    dividaComJuros = divida * juros
    valorParcela = dividaComJuros / parcela
    print('R$', round(dividaComJuros, 2), end='            ')
    print(round(valorJuros, 2), end='                  ')
    print(parcela, end='                        ')
    print('R$ ', round(valorParcela, 2))
    parcela += 3
