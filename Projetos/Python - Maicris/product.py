"""
Guitar Registration
"""


import utilities as util


CONST_FIELD_MODEL = "Modelo"
CONST_FIELD_BRAND = "Marca"
CONST_FIELD_YEAR = "Ano de Fabricação"
CONST_FIELD_COUNTRY = "Origem de Fabricação"
CONST_FIELD_COST = "Custo"
CONST_FIELD_DESCRIPTION = "Descrição"


def menu():
    util.ornament('Cadastro de Guitarras')
    util.ornament_two('-----SUAS OPÇÕES-----')
    print('[1] Cadastrar Guitarras\n'
          '[2] Alterar Guitarras\n'
          '[3] Pesquisar Guitarras\n'
          '[4] Listar Guitarras\n'
          '[5] Remover Estoque\n'
          '[6] SAIR')
    print('=' * 23)
    return util.get_int_value_with_range('Digite uma das opções: ', 1, 6)


def guitar_register(guitars: dict):
    """
    Registrar guitarra e suas especificações

    :param guitars: Características da guitarra ao cadastrá-la
    :return: None
    """
    serial = util.get_int_value('Informe o número de série da guitarra: ')
    model = str(input('Modelo da guitarra: \n'
                      ' -> SG\n'
                      ' -> Les Paul\n'
                      ' -> Explorer\n'
                      ' -> Flying V\n'
                      ' -> Telecaster\n'
                      ' -> Stratocaster\n'
                      'Escolha: ')).capitalize().strip()
    brand = input('Fabricante da guitarra: \n'
                  ' -> Gibson\n'
                  ' -> Fender\n'
                  ' -> Ibanez\n'
                  ' -> Yamaha\n'
                  ' -> Epiphone\n'
                  'Escolha (Se for outra, digite aqui): ').capitalize().strip()
    year = util.get_int_value_with_range('Ano de fabricação: ', 1931, util.actual_time())
    country = util.get_str_value('Origem da fabricação da guitarra: ').capitalize().strip()
    cost = util.get_float_value('Valor do produto: R$')
    description = input('Descrição da guitarra: ').capitalize().strip()
    guitars[serial] = {
        CONST_FIELD_MODEL: model,
        CONST_FIELD_BRAND: brand,
        CONST_FIELD_YEAR: year,
        CONST_FIELD_COUNTRY: country,
        CONST_FIELD_COST: cost,
        CONST_FIELD_DESCRIPTION: description
    }
    print('Guitarra cadastrada com sucesso!')


def guitar_edit(guitars: dict):
    """
    Altera dados dos registros da guitarra

    :param guitars: Exibe os dados dos registros de guitarras
    :return: None
    """
    serial = util.get_int_value('Número de série da guitarra: ')
    if serial in guitars:
        guitars.pop(serial)
        guitar_register(guitars)
        return True, "Especificações da guitarra alteradas com sucesso! "
    else:
        choice = util.yes_or_no_value('Guitarra não localizada. Deseja cadastrá-la?').strip().upper()[0]
        if choice == "S":
            guitar_register(guitars)
            print('Guitarra cadastrada com sucesso! ')
        else:
            print('Guitarra não localizada! ')


def search_guitar(guitars: dict):
    """
    Procura guitarras no banco de dados

    :param guitars: Possibilita a pesquisa de guitarras registradas
    :return: None
    """
    serial = util.get_int_value('Número de série da guitarra: ')
    if serial in guitars:
        print(f'Modelo da guitarra: {guitars[serial][CONST_FIELD_MODEL]}')
        print(f'Marca da guitarra: {guitars[serial][CONST_FIELD_BRAND]}')
        print(f'Ano de fabricação da guitarra: {guitars[serial][CONST_FIELD_YEAR]} ')
        print(f'Origem de fabricação da guitarra: {guitars[serial][CONST_FIELD_COUNTRY]} ')
        print(f'Custo da guitarra: {guitars[serial][CONST_FIELD_COST]} ')
        print(f'Descrição da guitarra: {guitars[serial][CONST_FIELD_DESCRIPTION]} ')
        util.sleep()
    else:
        choice = util.yes_or_no_value('Guitarra não localizada. Deseja cadastrá-la? [S/N]').strip().upper()[0]
        if choice == "S":
            guitar_register(guitars)
            print('Guitarra cadastrada com sucesso! ')
        else:
            print('Guitarra não localizada! ')


def list_guitar(guitars: dict):
    """
    Lista as guitarras contidas no dicionário

    :param guitars: Exibe as guitarras registradas no dicionário
    :return: None
    """
    for k, v in guitars.items():
        print(f'Número de série da guitarra e suas características -> {k} : {v}')
    util.sleep()


def stockpile_remove(guitars: dict):
    """
    Remoção de guitarras do estoque

    :param guitars: Identifica guitarras no estoque a serem removidos
    :return: None
    """
    serial = util.get_int_value('Digite o número de série da guitarra: ')
    if serial in guitars:
        choice = util.yes_or_no_value('Certeza que deseja remover a guitarra do estoque [S/N]: ').strip().upper()[0]
        if choice == 'S':
            del guitars[serial]
            print('Guitarra removida do estoque com sucesso! ')
        else:
            print('Nenhuma guitarra foi removida do estoque! ')


def main():
    guitars = {}
    while True:
        choice = menu()
        if choice == 1:
            guitar_register(guitars)
        if choice == 2:
            guitar_edit(guitars)
        if choice == 3:
            search_guitar(guitars)
        if choice == 4:
            list_guitar(guitars)
        if choice == 5:
            stockpile_remove(guitars)
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
