"""
Questão 02
Autor: Mauricio Kenzo De Albuquerque Kikuchi
"""


import utilidades as util


def print_units(unidades: list):
    """
    Exibe um print das unidades de conversão

    :param unidades: Lista de unidades de conversão
    :return: None
    """
    print('~' * 25)
    print('|', 'UNIDADES DE CONVERSÃO', '|')
    print('~' * 25)
    for c in unidades:
        print(f'→ {c}')
    print('~' * 25)


def menu(ano_luz: dict):
    """
    Solicitação ao usuário de valores numéricos e medidas
    necessárias para a conversão

    :param ano_luz: Dicionário das unidades de medidas e seus valores
    :return: Valor numérico, unidade de origem e unidade desejada
    """
    value = util.numeric_value('Valor a ser convertido: ')
    while True:
        initial_value = util.str_value('Converter de: ')
        if initial_value not in ano_luz:
            print('A unidade informada não foi encontrada no sistema.')
        else:
            break
    while True:
        final_value = util.str_value('Converter para: ')
        if final_value not in ano_luz:
            print('A unidade informada não foi encontrada no sistema.')
        else:
            break
    return value, initial_value, final_value


def conversion(v1: float, v2: str, v3: str, ano_luz):
    """
    Converte valores informados pelo usuário em diferentes unidades de medida

    :param v1: Valor numérico informado pelo usuário a ser convertido
    :param v2: Unidade de medida de origem
    :param v3: Unidade de medida a ser convertida
    :param ano_luz: Dicionário das unidades de medidas e seus valores
    :return: None
    """
    convert = (v1 * ano_luz[v3]) / (ano_luz[v2])
    print(f'Conversão: {v1}{v2} = {convert}{v3}')


def main():
    """
    Ponto principal do programa

    :return: None
    """
    ano_luz = {
        "pc": 0.31,
        "al": 1,
        "ae": 63241.09,
        "ml": 525960.23,
        "sl": 31557609.92
    }
    unidades = ["Parsec (pc)", "Ano-Luz (al)",
                "Unidade Astronômica (ae)",
                "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
    while True:
        print_units(unidades)
        v1, v2, v3 = menu(ano_luz)
        conversion(v1, v2, v3, ano_luz)
        choice = util.yes_or_no_value('Deseja converter outro número? [S/N]')
        if choice == 'S':
            print_units(unidades)
            v1, v2, v3 = menu(ano_luz)
            conversion(v1, v2, v3, ano_luz)
        else:
            print('A frota Alfa conta com você, oficial navegador!!!')
            break


if __name__ == '__main__':
    main()
