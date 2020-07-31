"""
Questão 01
Autor: Mauricio Kenzo De Albuquerque Kikuchi
"""


def print_menu():
    """
    Exibe um print do cardápio do restaurante

    :return: Escolha do cliente
    """
    print('~' * 67)
    print('=-=' * 10, 'CARDÁPIO', '=-=' * 9)
    print('~' * 67)
    print(f'| X-BURGUER {"•"*36} Pão e Hambúrguer |\n'
          f'| X-SALADA {"•"*29} Pão, Hambúrguer e Tomate |\n'
          f'| X-BACON {"•"*23} Pão, Hambúrguer, Tomate e Bacon |\n'
          f'| X-EGG {"•"*35} Pão, Hambúrguer e Ovo |\n'
          f'| X-TUDO {"•"*15} Pão, 2 Hamburgueres, Tomate, Bacon e Ovo |')
    print('~' * 67)
    choice = input('→ O que deseja pedir (0 para sair)?: ').lower().strip()
    return choice


def check_stock_ingredients(cardapio: dict, estoque: dict, choice: str):
    """
    Examinar a quantidade de ingredientes disponíveis

    :param cardapio: Dicionário de itens em um pedido
    :param estoque: Dicionário do estoque de ingredientes
    :param choice: Escolha do pedido do cliente
    :return: None
    """
    for c in cardapio[choice]:
        if estoque[c] > 0:
            estoque[c] -= 1
        else:
            print(f'Infelizmente acabou {c}')
            return
    print(f'Um {choice} saindo no capricho! ')


def main():
    """
    Ponto principal do programa

    :return: None
    """
    estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
    cardapio = {
        'x-burguer': ['pao', 'hamburguer'],
        'x-salada': ['pao', 'hamburguer', 'tomate'],
        'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
        'x-egg': ['pao', 'hamburguer', 'ovo'],
        'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
    }
    while True:
        choice = print_menu()
        if choice != "0":
            if choice not in cardapio:
                print('Item não localizado no cardápio.')
                print('Olhe novamente: ')
            else:
                check_stock_ingredients(cardapio, estoque, choice)
        else:
            print('O restaurante Boca Feliz conta com você!!!')
            break


if __name__ == '__main__':
    main()
