print('PANIFICADORA PÃO DE ONTEM - TABELA DE PREÇOS: ')
valorDoPao = float(input('Preço do pão na tabela: R$ '))
for c in range(1, 50+1, 1):
    print('{} --> R${:.2f}'.format(c, valorDoPao * c))
