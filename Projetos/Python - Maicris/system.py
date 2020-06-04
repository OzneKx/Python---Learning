"""
Sales System
"""


import utilities as util
import product as prod
import client as cli


def menu():
    util.ornament('Sistema de Vendas')
    util.ornament_two('-----SUAS OPÇÕES-----')
    print('[1] Criar Pedido\n'
          '[2] Cancelar Pedidos\n'
          '[3] Resumo de Pedidos\n'
          '[4] Relatório de Pedidos Gerais\n'
          '[5] Relatório de Pedidos por Cliente\n'
          '[6] SAIR')
    print('=' * 23)
    return util.get_int_value_with_range('Digite uma das opções: ', 1, 6)


def create_order():


def cancel_order():


def order_summary():


def general_order_report():


def specific_order_report():


def main():
    sales = {}
    while True:
        choice = menu()
        if choice == 1:
            create_order()
        if choice == 2:
            cancel_order()
        if choice == 3:
            order_summary()
        if choice == 4:
            general_order_report()
        if choice == 5:
            specific_order_report()
        if choice == 6:
            leave = util.yes_or_no_value('Certeza de que deseja sair do programa? [S/N]').strip().upper()[0]
            if leave == 'S':
                print('Volte sempre! ')
                break
            else:
                print('Você optou por não sair do programa! ')
                util.sleep()


if __name__ == '__main__':
    main()