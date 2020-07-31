"""
Guitar Registration
"""


# Importa modulos de utilidades
import utilities as util


CONST_FIELD_MODEL = "Modelo"
CONST_FIELD_BRAND = "Marca"
CONST_FIELD_YEAR = "Ano de Fabricação"
CONST_FIELD_COUNTRY = "Origem de Fabricação"
CONST_FIELD_COST = "Custo"
CONST_FIELD_DESCRIPTION = "Descrição"
CONST_FIELD_TOTAL = "Itens no Estoque"


def menu():
    """
    Exibe menu de opções

    :return: Opção escolhida pelo usuário
    """
    print('=' * 27)
    print(f'{"Cadastro de Guitarras":^27}')
    print('-' * 7, "Suas Opções", '-' * 7)
    print('[1] Cadastrar Guitarras\n'
          '[2] Alterar Guitarras\n'
          '[3] Pesquisar Guitarras\n'
          '[4] Listar Guitarras\n'
          '[5] Alterar Estoque\n'
          '[6] SAIR')
    print('=' * 27)
    return util.get_int_value_with_range('Digite uma das opções: ', 1, 6)


def guitar_register(serial: int, guitars: dict):
    """
    Registrar guitarra e suas especificações

    :param serial: Registro do número de série no dicionário
    :param guitars: Caracteristicas da guitarra ao cadastra-la
    :return: None
    """
    model = util.get_str_value('Modelo da guitarra: \n'
                               ' -> SG\n'
                               ' -> Les Paul\n'
                               ' -> Explorer\n'
                               ' -> Flying V\n'
                               ' -> Telecaster\n'
                               ' -> Stratocaster\n'
                               'Escolha: ')
    brand = util.get_str_value('Fabricante da guitarra: \n'
                               ' -> Gibson\n'
                               ' -> Fender\n'
                               ' -> Ibanez\n'
                               ' -> Yamaha\n'
                               ' -> Epiphone\n'
                               'Escolha (Se for outra, digite aqui): ')
    year = util.get_int_value_with_range('Ano de fabricação: ', 1931, util.actual_time())
    country = util.get_str_value('Origem da fabricação da guitarra: ')
    cost = util.get_float_value('Valor do produto: R$')
    description = input('Descrição da guitarra: ').title().strip()
    amount = util.get_int_value('Quantidade para adicionar: ')
    guitars[serial] = {
        CONST_FIELD_MODEL: model,
        CONST_FIELD_BRAND: brand,
        CONST_FIELD_YEAR: year,
        CONST_FIELD_COUNTRY: country,
        CONST_FIELD_COST: cost,
        CONST_FIELD_DESCRIPTION: description,
        CONST_FIELD_TOTAL: amount
    }


def guitar_add(guitars: dict):
    """
    Registrar guitarra e suas especificações

    :param guitars: Caracteristicas da guitarra ao cadastra-la
    :return: Se a guitarra já está registrada ou não
    """
    serial = util.get_int_value('Informe o número de série da guitarra: ')
    if serial in guitars:
        choice = util.yes_or_no_value('Guitarra já cadastrada! Deseja alterar seus dados? [S/N]')
        if choice == 'S':
            guitar_register(serial, guitars)
            return True, 'Dados da guitarra alterados com sucesso! '
        else:
            return False, 'Nenhum dado foi alterado ... '
    else:
        guitar_register(serial, guitars)
        return True, 'Guitarra cadastrada com sucesso! '


def guitar_edit(guitars: dict):
    """
    Altera dados dos registros da guitarra

    :param guitars: Exibe os dados dos registros de guitarras
    :return: Se a guitarra sofreu alterações nos dados ou não
    """
    serial = util.get_int_value('Informe o número de série da guitarra a ser editada: ')
    if serial in guitars:
        guitar_register(serial, guitars)
        return True, 'Cliente alterado com sucesso! '
    else:
        choice = util.yes_or_no_value('Guitarra não localizado! Deseja cadastrá-la? [S/N]')
        if choice == 'S':
            guitar_register(serial, guitars)
            return True, 'Guitarra cadastrada com sucesso! '
        else:
            return False, 'Guitarra não foi cadastrada... '


def search_guitar(guitars: dict):
    """
    Procura guitarras no banco de dados

    :param guitars: Possibilita a pesquisa de guitarras registradas
    :return: Se a guitarra foi encontrada ou não
    """
    serial = util.get_int_value('Informe o número de série da guitarra que deseja pesquisar: ')
    if serial in guitars:
        print('-' * 57)
        print('=' * 17, 'Guitarra Encontrada', '=' * 18)
        print('-' * 57)
        print(f'| N° de série da guitarra: {serial:>28} |\n'
              f'| {CONST_FIELD_MODEL}: {guitars[serial][CONST_FIELD_MODEL]:>45} |\n'
              f'| {CONST_FIELD_BRAND}: {guitars[serial][CONST_FIELD_BRAND]:>46} |\n'
              f'| {CONST_FIELD_YEAR}: {guitars[serial][CONST_FIELD_YEAR]:>34} |\n'
              f'| {CONST_FIELD_COUNTRY}: {guitars[serial][CONST_FIELD_COUNTRY]:>31} |\n'
              f'| {CONST_FIELD_COST}: {guitars[serial][CONST_FIELD_COST]:>46} |\n'
              f'| {CONST_FIELD_DESCRIPTION}: {guitars[serial][CONST_FIELD_DESCRIPTION]:>42} |\n'
              f'| {CONST_FIELD_TOTAL}: {guitars[serial][CONST_FIELD_TOTAL]:>35} |')
        print('-' * 57)
    else:
        choice = util.yes_or_no_value('Guitarra não localizada. Deseja cadastrá-la? [S/N]')
        if choice == "S":
            guitar_register(serial, guitars)
            print('Guitarra cadastrada com sucesso! ')
        else:
            print('Guitarra não localizada! ')


def list_guitar(guitars: dict):
    """
    Lista as guitarras registradas

    :param guitars: Exibe as guitarras registradas no dicionário
    :return: None
    """
    if len(guitars) > 0:
        available_guitars(guitars)
    else:
        print('Não há guitarras disponíveis no estoque para listá-las. ')


def stockpile_modify(guitars: dict):
    """
    Adicionar ou remover guitarras do estoque

    :param guitars: Identifica guitarras no estoque a serem removidos
    :return: None
    """
    serial = util.get_int_value('Digite o número de série da guitarra: ')
    if serial in guitars:
        choice = util.get_int_value_with_range('[1] Adicionar itens ao estoque\n'
                                               '[2] Remover itens do estoque\n'
                                               'Escolha: ', 1, 2)
        if choice == 1:
            add = util.get_int_value('Quantidade de itens para adicionar: ')
            guitars[serial][CONST_FIELD_TOTAL] += add
            print(f'{add} itens foram adicionados com sucesso! ')
        else:
            subtract = util.get_int_value('Quantidade de itens para remover: ')
            if guitars[serial][CONST_FIELD_TOTAL] - subtract < 0:
                print(f'A quantia de itens no estoque não pode ser inferior a zero...')
                choice = util.yes_or_no_value('Gostaria de ver quantos itens você tem no momento? [S/N]')
                if choice == 'S':
                    print(f'Existem {guitars[serial][CONST_FIELD_TOTAL]} itens no estoque.')
                else:
                    print('Você optou por não visualizar o total de itens no estoque...')
            guitars[serial][CONST_FIELD_TOTAL] -= subtract
            print('Itens foram removidos com sucesso! ')
    else:
        choice = util.yes_or_no_value('Guitarra não localizada no estoque. Deseja adiciona-la? [S/N]')
        if choice == "S":
            guitar_register(serial, guitars)
            print('Guitarra adicionada ao estoque com sucesso! ')
        else:
            print('Nenhuma guitarra foi reposta no estoque... ')


def available_guitars(guitars: dict):
    """
    Exibe as guitarras disponiveis no estoque

    :param guitars: Mostra as guitarras no estoque
    :return: None
    """
    print('-' * 57)
    print('=' * 17, 'Produtos Disponíveis', '=' * 18)
    print('-' * 57)
    for c in guitars:
        print(f'| N° de série da guitarra: {c:>28} |\n'
              f'| {CONST_FIELD_MODEL}: {guitars[c][CONST_FIELD_MODEL]:>45} |\n'
              f'| {CONST_FIELD_BRAND}: {guitars[c][CONST_FIELD_BRAND]:>46} |\n'
              f'| {CONST_FIELD_YEAR}: {guitars[c][CONST_FIELD_YEAR]:>34} |\n'
              f'| {CONST_FIELD_COUNTRY}: {guitars[c][CONST_FIELD_COUNTRY]:>31} |\n'
              f'| {CONST_FIELD_COST}: {guitars[c][CONST_FIELD_COST]:>46} |\n'
              f'| {CONST_FIELD_DESCRIPTION}: {guitars[c][CONST_FIELD_DESCRIPTION]:>42} |\n'
              f'| {CONST_FIELD_TOTAL}: {guitars[c][CONST_FIELD_TOTAL]:>35} |')
        print('-' * 57)
    print('')


def main(guitars: dict):
    """
    Ponto principal do programa
    """
    while True:
        choice = menu()
        if choice == 1:
            res, resp = guitar_add(guitars)
            print(resp)
        if choice == 2:
            res, resp = guitar_edit(guitars)
            print(res)
        if choice == 3:
            search_guitar(guitars)
        if choice == 4:
            list_guitar(guitars)
        if choice == 5:
            stockpile_modify(guitars)
        if choice == 6:
            leave = util.yes_or_no_value('Certeza de que deseja sair do programa? [S/N]')
            if leave == 'S':
                print('Volte sempre! ')
                util.save_in_file_dict("guitarras", guitars)    # Salvar um dicionário em um arquivo binário
                break
            else:
                print('Você optou por não sair do programa... ')


if __name__ == '__main__':
    var = util.file_read_bin("guitarras")   # Leitura do arquivo, porém, caso não exista, será criado um
    main(var)
