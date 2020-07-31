"""
Utilidades
Autor: Mauricio Kenzo De Albuquerque Kikuchi
"""


def numeric_value(message: str):
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
            print('Digite um valor númerico! ')


def str_value(message: str):
    """
    Valida dados informados pelo usuário

    :param message: Mensagem do input exibida ao usuário
    :return palavra: Retorna o input do usuário
    """
    report = ''
    while True:
        word = input(message).lower()
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
            print('Espaços vazios não são permitidos! Insira algo, por favor!')


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
