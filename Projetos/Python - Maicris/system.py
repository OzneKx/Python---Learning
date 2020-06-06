"""
Sales System

sales = {
    id_venda: {                         sales = { id_venda: {id_client: "bla", products: [ {id_product: "asd", quantidade: ?}, {id_product: "asd", quantidade: ?} ], total: ? } }
        id_client: "",
        guitars: [
            {
                id_product: "",
                quant: 0
            },
            {
                id_product: "".
                quant: 1
            }
        ],
        total: 100
    }
}
"""


import utilities as util
import guitars as gui
import clients as cli
import pickle


CONST_FIELD_IDENTIFICATION = "Identidade"
CONST_FIELD_QUANTITY = "Quantidade"
CONST_FIELD_VALUE = "Valor Total"


def menu():
    print('Sistema de Vendas')
    print('-----SUAS OPÇÕES-----')
    print('[1] Criar Pedido\n'
          '[2] Cancelar Pedido\n'
          '[3] Resumo de Pedidos\n'
          '[4] Relatório de Pedidos Gerais\n'
          '[5] Relatório de Pedidos por Cliente\n'
          '[6] SAIR')
    print('=' * 23)
    return util.get_int_value_with_range('Digite uma das opções: ', 1, 6)


def create_order(clients: dict, guitars: dict, sales: dict, identification: int, serial: int,
                 cost: float):
    identification = util.get_int_value('Informe sua identidade: ')
    if identification not in clients:
        choice = util.yes_or_no_value('Não é cadastrado ainda. Gostaria de se cadastrar? [S/N]')
        if choice == 'N':
            print('Você optou por não se cadastrar, logo não poderá fazer nenhuma compra... Se cadastre antes! ') 
        else:
            cli.client_register(identification, clients)
            print('Cadastro efetuado com sucesso! Agora poderá fazer compras! ')
            print('Estas são as guitarras disponíveis no estoque: ')
            for k, v in guitars.items():
                print(f'{k} = {v}')
            while True:
                buy = util.get_int_value('Número de série da guitarra que gostaria de comprar: ')
                if buy not in guitars:
                    print('Guitarra não disponível, tente novamente mais tarde!  ')
                else:
                    print(f'{guitars[serial][gui.CONST_FIELD_MODEL][gui.CONST_FIELD_BRAND]} é uma ótima escolha! ')
                    amount = util.get_int_value('Informe quantas unidades gostaria de comprar: ')
                    if guitars[serial][gui.CONST_FIELD_TOTAL] - amount > 0:
                        guitars[serial][gui.CONST_FIELD_TOTAL] = amount
                        cost = guitars[serial][gui.CONST_FIELD_COST] * amount
                        sales[order] = {clients[identification], guitars[serial], CONST_FIELD_VALUE: cost}
                        print(f'Pedido efetuado, {clients[cli.CONST_FIELD_NAME]}! ')
                        more = util.yes_or_no_value('Gostaria de comprar mais uma guitarras? [S/N]')
                        if more == 'N':
                            print('Agradeço por ter comprado o produto! Volte sempre! ')
                        else:
                            continue
                    else:
                        print('Não temos mais itens como este no estoque... Volte em outro momento :/')



def cancel_order():



def order_summary():
    print('-' * 10, 'Resumo de pedidos', '-' * 10)
    print()

def general_order_report():



def specific_order_report():





def main():
    file_guitars = 'guitarras'
    file_clients = 'cliente'
    file_sales = 'sale'
    database = util.file_read_bin(CONST_FILE_NAME)
    if "clients" in database:
        clients = database["Clients"]
    if "products" in database:
        guitars = database["Products"]
    if "sales" in database:
        sales = database["sales"]
    while True:
        choice = menu()
        if choice == 1:
            create_order(clients, guitars, sales)
        elif choice == 2:
            cancel_order()
        elif choice == 3:
            cli.main(clients)  #Maicris fez
            order_summary()
        elif choice == 4:
            general_order_report()
        elif choice == 5:
            specific_order_report()
        elif choice == 6:
            leave = util.yes_or_no_value('Certeza de que deseja sair do programa? [S/N]')
            if leave == 'S':
                print('Volte sempre! ')
                break
            else:
                print('Você optou por não sair do programa! ')

    database["clients"] = clients
    database["guitars"] = guitars
    database["sales"] = sales
    util.file_write_bin(CONST_FILE_NAME, database)


if __name__ == '__main__':
    main()