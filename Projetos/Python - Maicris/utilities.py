"""
Module Utilities
"""


from datetime import date
import pickle


def ornament(txt: str):
    """
    Enfeite de textos, de acordo com teu tamanho

    :param txt: Texto a ser exibido
    :return: None
    """
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))


def ornament_two(text: str):
    """
    Outro enfeite de textos, de acordo com teu tamanho

    :param text: Texto a ser exibido
    :return: None
    """
    print('=' * len(text))
    print(text)
    print('=' * len(text))


def actual_time():
    """
    Importa a função date da library do Python

    :return: Retorna a data do ano atual
    """
    current = date.today().year
    return current


def sleep():
    """
    Importa a função sleep da library do Python

    :return: None
    """
    from time import sleep
    sleep(1.5)


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
            choice = int(input(message).strip())
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
    :return palavra: None
    """
    while True:
        word = input(message).strip()
        if not word.isalpha():
            print('INVÁLIDO! Utilize letras! ')
        else: 
            break


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


