tuplaListagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
                 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
                 'Canetas', 22.30, 'Livro', 34.90)
print('=-=' * 14)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=-=' * 14)
for position in range(0, len(tuplaListagem)):
    if position % 2 == 0:
        print(f'{tuplaListagem[position]:.<30}', end='')
    else:
        print(f'R$ {tuplaListagem[position]:>8}')
print('=-=' * 14)