"""
Client Registration
"""


# Importa modulos de utilidades
import utilities as util


CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


def menu_clients():
    """
    Exibe menu de opções

    :return: Opção escolhida pelo usuário
    """
    print('=' * 30)
    print(f'{"Cadastro de Clientes":^30}')
    print('-' * 8, "Suas Opções", '-' * 8)
    print('[1] Cadastrar Cliente\n'
          '[2] Alterar dados de cliente\n'
          '[3] Excluir cliente\n'
          '[4] Pesquisar Cliente\n'
          '[5] Zerar Banco de Dados\n'
          '[6] Listar Clientes\n'
          '[7] SAIR')
    print('=' * 30)
    return util.get_int_value_with_range('Digite uma das opções: ', 1, 7)


def client_register(identification: int, clients: dict):
    """
    Registrar clientes com seus dados

    :param identification: Registro da identificação do cliente no dicionário
    :param clients: Dados do cliente para cadastrá-la no dicinário
    :return: None
    """
    name = util.get_str_value('Informe o nome do cliente: ')
    city = util.get_str_value('Informe a cidade do cliente: ')
    age = util.get_int_value_with_range('Digite a idade do cliente: ', 18, 120)
    clients[identification] = {
        CONST_FIELD_NAME: name,
        CONST_FIELD_CITY: city,
        CONST_FIELD_AGE: age
    }


def client_add(clients: dict):
    """
    Registrar clientes com seus dados

    :param clients: Dados do cliente para cadastrá-la
    :return: Se o cliente já está registrado ou não
    """
    identification = util.get_int_value('Informe a identidade do cliente: ')
    if identification in clients:
        choice = util.yes_or_no_value('Cliente já cadastrado! Deseja alterar seus dados? [S/N]')
        if choice == 'S':
            client_register(identification, clients)
            return True, 'Dados do cliente alterados com sucesso! '
        else:
            return False, 'Nenhum dado foi alterado ... '
    else:
        client_register(identification, clients)
        return True, 'Cliente cadastrado com sucesso! '


def client_edit(clients: dict):
    """
    Altera dados dos registros do cliente

    :param clients: Exibe os dados dos registros do cliente
    :return: Se o cliente sofreu alterações nos dados ou não
    """
    identification = util.get_int_value('Informe a identidade do cliente a ser editado: ')
    if identification in clients:
        client_register(identification, clients)
        return True, 'Cliente alterado com sucesso! '
    else:
        choice = util.yes_or_no_value('Cliente não localizado. Deseja cadastrá-lo? [S/N]')
        if choice == 'S':
            client_register(identification, clients)
            return True, 'Cliente cadastrado com sucesso! '
        else:
            return False, 'Cliente não foi cadastrado... '


def client_del(clients: dict):
    """
    Remoção de clientes específicos do banco de dados através de sua identificação

    :param clients: Identifica clientes no banco de dados a serem removidos através de sua identificação
    :return: None
    """
    identification = util.get_int_value('Informe a identidade do cliente que deseja remover: ')
    if identification in clients:
        choice = util.yes_or_no_value('Deseja mesmo deletar o cliente? [S/N]')
        if choice == 'S':
            clients.pop(identification)
            return True, 'Cliente deletado com sucesso! '
        else:
            return False, 'Cliente não foi deletado... '
    else:
        choice = util.yes_or_no_value('Cliente não localizado. Deseja cadastrá-lo? [S/N]')
        if choice == 'S':
            client_register(identification, clients)
            return True, 'Cliente cadastrado com sucesso! '
        else:
            return False, 'Cliente não foi cadastrado... '


def client_search(clients: dict):
    """
    Pesquisa clientes no banco de dados atraves de suas identidades

    :param clients: Possibilita a pesquisa de clientes registradas
    :return: Se o cliente foi encontrado ou não
    """
    identification = util.get_int_value('Informe a identidade do cliente que deseja pesquisar: ')
    if identification in clients:
        print('-' * 33)
        print('-' * 6, 'Cliente Encontrado', '-' * 7)
        print('-' * 33)
        print(f'| Nome  do  cliente: {clients[identification][CONST_FIELD_NAME]:>10} | \n'
              f'| Cidade do cliente: {clients[identification][CONST_FIELD_CITY]:>10} | \n'
              f'| Idade  do cliente: {clients[identification][CONST_FIELD_AGE]:>10} |')
        print('-' * 33)
    else:
        choice = util.yes_or_no_value('Cliente não localizado. Deseja cadastra-lo? [S/N]')
        if choice == "S":
            client_register(identification, clients)
            print('Cliente cadastrado com sucesso! ')
        else:
            print('Cliente não localizado nos cadastros... ')


def database_clear(clients: dict):
    """
    Remove clientes do banco de dados

    :param clients: Remove clientes do banco de dados
    :return: None
    """
    if len(clients) > 0:
        choice = util.yes_or_no_value('Certeza de que gostaria de deletar o banco de dados? [S/N]')
        if choice == 'S':
            clients.clear()
            print('Banco de dados deletado com sucesso! ')
        else:
            print('O banco de dados não foi deletado... ')
    else:
        print('Não há como zerar o banco de dados, pois já está vazio! ')


def list_clients(clients: dict):
    """
    Lista os clientes registrados

    :param clients: Exibe os clientes registrados no dicionário
    :return: None
    """
    if len(clients) > 0:
        existent_clients(clients)
    else:
        print('Não existem clientes registrado! ')


def existent_clients(clients: dict):
    """
    Exibe os clientes registrados

    :param clients: Mostra os clientes cadastrados
    :return: None
    """
    print('-' * 57)
    print('=' * 17, 'Clientes Registrados', '=' * 18)
    print('-' * 57)
    for c in clients:
        print(f'| Identidade do cliente: {c:>30} |\n'
              f'| Nome  do  cliente: {clients[c][CONST_FIELD_NAME]:>34} | \n'
              f'| Cidade do cliente: {clients[c][CONST_FIELD_CITY]:>34} | \n'
              f'| Idade  do cliente: {clients[c][CONST_FIELD_AGE]:>34} |')
        print('-' * 57)
    print('')


def main(clients: dict):
    """
    Ponto principal do programa

    :return: None
    """
    while True:
        choice = menu_clients()
        if choice == 1:
            res, resp = client_add(clients)
            print(resp)
        elif choice == 2:
            res, resp = client_edit(clients)
            print(resp)
        elif choice == 3:
            res, resp = client_del(clients)
            print(resp)
        elif choice == 4:
            client_search(clients)
        elif choice == 5:
            database_clear(clients)
        elif choice == 6:
            list_clients(clients)
        elif choice == 7:
            leave = util.yes_or_no_value('Certeza de que deseja sair do programa? [S/N]')
            if leave == 'S':
                print('Volte sempre! ')
                util.save_in_file_dict("cliente", clients)  # Salvar um dicionário em um arquivo binário
                break
            else:
                print('Você optou por não sair do programa! ')


if __name__ == '__main__':
    var = util.file_read_bin("cliente")     # Leitura do arquivo, porém, caso não exista, será criado um
    main(var)
