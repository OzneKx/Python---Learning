"""
Module Utilities
"""


from datetime import date
import pickle


def actual_time():
    """
    Importa a função date da library do Python

    :return: Retorna a data do ano atual
    """
    current = date.today().year
    return current


def get_int_value_with_range(message: str, min_value: int, max_value: int) -> int:
    """
    Valida dados inteiros em um determinado range

    :param message: Retorna valor
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna a opção escolhida dentro do range
    """
    while True:
        try:
            choice = int(input(message))
        except ValueError:
            print('Formato inválido! Digite um NÚMERO!')
            continue
        if not min_value <= choice <= max_value:
            print(f'Opção inválida! Sua escolha deve ser entre {min_value} e {max_value}...')
        else:
            return choice


def get_int_value(message: str):
    """
    Valida dados informados pelo usuário

    :param message: Mensagem do input exibida ao usuário
    :return number: Valor inteiro informado pelo usuário
    """
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('Digite um número inteiro! ')


def get_float_value(message: str):
    """
    Valida dados informados pelo usuário

    :param message: Mensagem do input exibida ao usuário
    :return number: Valor numérico informado pelo usuário
    """
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print('Digite um número! ')


def get_str_value(message: str):
    """
    Valida dados informados pelo usuário

    :param message: Mensagem do input exibida ao usuário
    :return palavra: Retorna o input do usuário
    """
    report = ''
    while True:
        word = input(message).title()
        if len(word) != 0:
            for c in word:
                if c.isnumeric():
                    report = True
                else:
                    report = False
            if report:
                print('Inválido! Insira apenas letras! ')
            else:
                return word
        else:
            print('Espaços vazios não são permitidos! Insira algo, por favor! ')


def yes_or_no_value(message: str):
    """
    Exibe mensagem de confirmação na tentativa de remoção do estoque

    :param message: Mensagem exibida ao usuário antes de remover o estoque
    :return: Retorna a escolha feita pelo usuário
    """
    while True:
        choice = input(f'{message}: ').strip().upper()[0]
        if choice in 'SN':
            return choice
        else:
            print('Inválido! Escolha [S] - sim ou [N] - não')


def save_in_file_dict(name: str, dict_name: dict):
    """
    Salvar um dicionário em um arquivo binário.

    :param name: Nome do Arquivo.
    :param dict_name: Nome do Dicionário.
    :return: Arquivo salvo
    """
    with open(name, "wb") as f:
        pickle.dump(dict_name, f)
    return


def file_read_bin(filename: str) -> dict:
    """
    Leitura do arquivo, porém, caso não exista, será criado um

    :param filename: Nome do arquivo de gravação
    :return: Lista com os dados lidos
    """
    content = {}
    try:
        file = open(filename, "rb")
        content = pickle.load(file)
        file.close()
        return content
    except FileNotFoundError:
        with open(filename, "wb") as f:
            pickle.dump(content, f)
        file = open(filename, "rb")
        content = pickle.load(file)
        file.close()
    return content
