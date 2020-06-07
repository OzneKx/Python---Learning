"""
Sales System
"""


import utilities as util
import guitars as gui
import clients as cli


__version__ = "1.0"
__author__ = "Kenzo De Albuquerque"
__credits__ = "Kenzo De Albuquerque"


CONST_FIELD_ORDER = "Produtos"
CONST_FIELD_VALUE = "Valor Total"
CONST_FIELD_QUANTITY = "Quantidade"
CONST_FIELD_IDENTIFICATION = "Identidade"


def menu():
    """
    Exibe menu de opções

    :return: Opção escolhida pelo usuário
    """
    print('=' * 37)
    print(f'{"Sistema de Vendas":^38}')
    print('-' * 12, "Suas Opções", '-' * 12)
    print('[1] Criar Pedido\n'
          '[2] Cancelar Pedido\n'
          '[3] Resumo de Pedidos\n'
          '[4] Relatório de Pedidos Gerais\n'
          '[5] Relatório de Pedidos por Cliente\n'
          '[6] Acessar Módulo de Clientes\n'
          '[7] Acessar Módulo de Guitarras\n'
          '[8] SAIR')
    print('=' * 37)
    return util.get_int_value_with_range('Digite uma das opções: ', 1, 8)


def create_order(clients: dict, guitars: dict, sales: dict, identification: int):
    """
    Realizar pedidos de guitarras por usuários cadastrados

    :param clients: Dicionario de clientes cadastrados
    :param guitars: Dicionário de guitarras registradas
    :param sales: Dicionário de pedidos, contendo o cliente e o produto
    :param identification: Identidade do cliente ao comprar
    :return: None
    """
    print('Estas são as guitarras disponíveis no estoque: ')
    for k, v in guitars.items():
        print(f'{k} = {v}')
    order = util.get_int_value('Número do pedido: ')
    if order not in sales:
        while True:
            serial = util.get_int_value('Número de série da guitarra que gostaria de comprar: ')
            if serial not in guitars:
                print('Guitarra não disponível, tente novamente mais tarde! ')
            else:
                amount = util.get_int_value('Informe quantas unidades gostaria de comprar: ')
                if guitars[serial][gui.CONST_FIELD_TOTAL] - amount > 0:
                    guitars[serial][gui.CONST_FIELD_TOTAL] -= amount
                    cost = guitars[serial][gui.CONST_FIELD_COST] * amount
                    sales[order] = {CONST_FIELD_IDENTIFICATION: clients[identification],
                                    CONST_FIELD_ORDER:
                                        [{gui.CONST_FIELD_MODEL: guitars[serial][gui.CONST_FIELD_MODEL],
                                            gui.CONST_FIELD_BRAND: guitars[serial][gui.CONST_FIELD_BRAND],
                                            CONST_FIELD_QUANTITY: amount,
                                            CONST_FIELD_VALUE: cost}]}
                    print('Pedido efetuado! ')
                    more = util.yes_or_no_value('Gostaria de comprar mais uma guitarras? [S/N]')
                    if more == 'N':
                        print('Agradeço por ter comprado o produto! Volte sempre! ')
                        break
                    else:
                        continue
                else:
                    print(f'O estoque contém apenas {guitars[serial][gui.CONST_FIELD_TOTAL]} produtos.\n'
                          f'Portanto, ele não pode se esgotar :) ')
    else:
        print('Insira outro número de pedido! ')


def cancel_order(sales: dict):
    """
     Cancela pedido efetuado pelo cliente

     :param sales: Remove clientes do banco de dados
     :return: None
     """
    choice = util.yes_or_no_value('Certeza de que gostaria de cancelar o pedido? [S/N]')
    if choice == 'S':
        order = util.get_int_value('Número do pedido: ')
        sales.pop(order)
        print('Pedido cancelado com sucesso! ')
    else:
        print('O pedido não foi cancelado... ')


def order_summary(sales: dict):
    """
    Resumo de pedidos efetuados

    :param sales: Exibe vendas efetuadas e seus detalhes
    :return: None
    """
    order = util.get_int_value('Informe o número do pedido: ')
    if order in sales:
        print('-' * 13, 'Resumo do Pedido', '-' * 13)
        print(f'| Nome  do  comprador: {sales[order][CONST_FIELD_IDENTIFICATION][cli.CONST_FIELD_NAME]:>20}|')
        print(f'| Modelo  da guitarra: {sales[order][CONST_FIELD_ORDER][0][gui.CONST_FIELD_MODEL]:>20}|')
        print(f'| Marca  da  guitarra: {sales[order][CONST_FIELD_ORDER][0][gui.CONST_FIELD_BRAND]:>20}|')
        print(f'| Quantidade comprada: {sales[order][CONST_FIELD_ORDER][0][CONST_FIELD_QUANTITY]:>20}|')
        print(f'| Total (REAIS -> R$): {sales[order][CONST_FIELD_ORDER][0][CONST_FIELD_VALUE]:>20.2f}|')
        print('-' * 44)
    else:
        print('Nenhum pedido corresponde ao número informado... Tente novamente! ')


def general_order_report(sales: dict):
    """
    Lista as vendas gerais que foram feitas

    :param sales: Exibe as vendas efetuadas
    :return: None
    """
    if len(sales) > 0:
        for k, v in sales.items():
            print(f'{k} : {v}')
    else:
        print('Nenhuma venda foi feita até então')


def specific_order_report(sales: dict):
    """
    Lista as vendas específicas que foram feitas

    :param sales: Exibe as vendas pelo respectivo numero de pedido
    :return: None
    """
    if len(sales) > 0:
        order = util.get_int_value('Número do pedido que gostaria de buscar: ')
        if order not in sales:
            print('Número de pedido não encontrado! ')
        else:
            print(sales[order])
    else:
        print('Nenhuma venda foi feita até então')


def main():
    """
    Ponto principal do programa

    :return: None
    """
    guitars = util.file_read_bin('guitarras')
    clients = util.file_read_bin('cliente')
    sales = util.file_read_bin('sales')
    while True:
        choice = menu()
        if choice == 1:
            identification = util.get_int_value('Informe sua identidade: ')
            if identification not in clients:
                choice = util.yes_or_no_value('Não cadastrado. Gostaria de se cadastrar? [S/N]')
                if choice == 'N':
                    print('Se cadastre antes, caso queira efetuar uma compra! ')
                else:
                    cli.client_register(identification, clients)
                    print('Cadastro efetuado com sucesso! Agora poderá fazer compras! ')
                    create_order(clients, guitars, sales, identification)
            else:
                create_order(clients, guitars, sales, identification)
        elif choice == 2:
            cancel_order(sales)
        elif choice == 3:
            order_summary(sales)
        elif choice == 4:
            general_order_report(sales)
        elif choice == 5:
            specific_order_report(sales)
        elif choice == 6:
            cli.main(clients)
        elif choice == 7:
            gui.main(guitars)
        elif choice == 8:
            leave = util.yes_or_no_value('Certeza de que deseja sair do programa? [S/N]')
            if leave == 'S':
                print('Volte sempre! ')
                util.save_in_file_dict("sales", sales)
                break
            else:
                print('Você optou por não sair do programa! ')


if __name__ == '__main__':
    main()
