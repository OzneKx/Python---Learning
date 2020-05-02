def area(lado, comprimento):
    print(f'Lado = {lado} e Comprimento = {comprimento}')
    A = (lado * comprimento)
    print(f'{lado}m X {comprimento}m = {A}m²')


print('==== Área do terreno ====')
lado = float(input('Lado do terreno (m): '))
comprimento = float(input('Comprimento do terreno (m): '))
area(lado, comprimento)