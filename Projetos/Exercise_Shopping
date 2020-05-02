print('{:=^}'.format(' LOJAS ALBUQUERQUE '))
custoProduto = float(input('Valor das compras: R$ '))
print('Qual o método de pagamento gostaria de fazer? \n'
      '[1] DINHEIRO/CHEQUE\n'
      '[2] CARTÃO')
digiteEscolhaMetodoPagamento = int(input('Digite a opção desejada: '.strip()))
if digiteEscolhaMetodoPagamento == 1:
    print('Você recebeu um desconto de 10%. O produto que antes custava R${:.2f}, passou a custar R${:.2f} '.format(custoProduto, (custoProduto * 0.9)))
elif digiteEscolhaMetodoPagamento == 2:
    print('Em quantas vezes deseja pagar no cartão? \n'
          '[1] À VISTA\n'
          '[2] EM 2X\n'
          '[3] 3X OU MAIS NO CARTÃO')
    digiteEscolhaMetodoPagamento2 = int(input('Digite a opção desejada: '.strip()))
    if digiteEscolhaMetodoPagamento2 == 1:
        print('Você recebeu um desconto de 5%. O produto que antes custava R${:.2f}, passou a custar R${:.2f} '.format(custoProduto, (custoProduto * 0.95)))
    elif digiteEscolhaMetodoPagamento2 == 2:
        print('O produto custará R${:.2f} '.format(custoProduto))
    elif digiteEscolhaMetodoPagamento2 == 3:
        print('Você pagará um juros de 20% sobre o produto. O produto que antes custava R${:.2f}, passou a custar R${:.2f} '.format(custoProduto, (custoProduto * 1.2)))
    elif digiteEscolhaMetodoPagamento2 > 3:
         print('\033[31mOPÇÃO INVALIDA DE PAGAMENTO! TENTE NOVAMENTE! ')
elif digiteEscolhaMetodoPagamento > 2:
    print('\033[31mOPÇÃO INVALIDA DE PAGAMENTO! TENTE NOVAMENTE! ')