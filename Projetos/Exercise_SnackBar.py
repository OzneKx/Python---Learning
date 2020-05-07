print('Especificação   Código   Preco')
print('Cachorro Quente 100     R$ 1,20')
print('Bauru Simples   101     R$ 1,30')
print('Bauru Com Ovo   102     R$ 1,50')
print('Hamburger       103     R$ 1,20')
print('Cheeseburger    104     R$ 1,30')
print('Refrigerante    105     R$ 1,00')
listaCodigosLanchonete = [100, 101, 102, 103, 104, 105]
listaPrecosLanchonete = [1.2, 1.3, 1.5, 1.2, 1.3, 1.0]
listaPedidos = []
codigoPedido = True
numeroPedido = 1
while codigoPedido != 0:
    codigoPedido = int(input('Digite o código do pedido: '))
    if codigoPedido == 0:
        break
    else:
        while codigoPedido not in listaCodigosLanchonete:
            print('Este item não pertence à nenhum pedido! ')
            codigoPedido = int(input('Digite o código do pedido: '))
        codigos = listaCodigosLanchonete.index(codigoPedido)
        quantidadePedidos = int(input('Quantidade de pedidos: '))
        valorPedido = (listaPrecosLanchonete[codigos] * quantidadePedidos)
        listaPedidos.append(valorPedido)
    numeroPedido += 1
notaPedido = 0
for c in range(numeroPedido - 1):
    print('Pedido nº{} = R${:.2f}'.format((notaPedido + 1), listaPedidos[notaPedido]))
    notaPedido += 1
print('Total: R${}'.format(sum(listaPedidos)))