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


CONST_FIELD_QUANTITY = "Quantidade"
CONST_FIELD_VALUE = "Valor Total"
CONST_FILE_NAME = "database"


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


def create_order(clients: dict, guitars: dict, sales: dict, identification: int, serial: int):
    util.file_read_bin("cliente")
    resp = cli.client_search(clients)
    if resp:
        print('Venda será prosseguida! ')
        ans = gui.search_guitar(guitars)
        if ans:
            print('Guitarra disponível! ')


        else:
            print('Guitarra não encontrada... ')
            choice = util.yes_or_no_value('Guitarra não localizado! Deseja cadastrá-la? [S/N]')
            if choice == 'S':
                gui.guitar_register(serial, guitars)
                return True, 'Guitarra cadastrada com sucesso! '
            else:
                return False, 'Guitarra não foi cadastrada... '
    else:
        print('Cliente não cadastrado no sistema... ')
        choice = util.yes_or_no_value('Cliente não localizado. Deseja cadastra-lo? [S/N]')
        if choice == "S":
            cli.client_register(identification, clients)
            print('Cliente cadastrado com sucesso! ')
        else:
            print('Cliente não foi cadastrado... ')


def cancel_order():


def order_summary():


def general_order_report():


def specific_order_report():


def main():
    # database = {
        #"Cliente": clients,
        #"Guitarras": guitars,
        #"Venda": sales
    # }

    sales = {}
    guitars = {}
    clients = {}

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