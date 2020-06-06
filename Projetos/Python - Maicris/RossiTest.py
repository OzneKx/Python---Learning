import pickle

CONST_NAME_NAME = "name"
CONST_NAME_SIZE = "tamanho"
CONST_NAME_QUANTITY = "quantidade"
CONST_NAME_PRICE = "preço"


def get_int_value_with_range(message: str, min_value: int, max_value: int) -> int:
    """
    Valida dados inteiros em um determinado range

    :param message: A mensagem a ser exibida
    :param min_value: Valor inteiro mínimo
    :param max_value: Valor inteiro máximo
    :return: Retorna a opção escolhida dentro do range
    """
    while True:
        try:
            op = int(input(message + ": "))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print("Opção inválida: escolha um número de", min_value, "a", max_value)
        else:
            return op


def get_yes_no_value(message: str) -> str:
    """
    Valida opções de sim e não

    :param message: A mensagem a ser exibida
    :return: Retorna a opção escolhida s/n
    """
    while True:
        op = input(message + " (s/n): ")
        if op == 's' or op == 'n':
            return op
        else:
            print("Opção inválida: escolha s (sim) ou n (não)")


def remove(products):
    """


    :param products:
    :return:
    """
    name = products(input("Qual camiseta deseja remover: ")
    if name not in products:
        print("Camiseta não encontrada")
    else:
        products.pop(name)
        print("Removido com sucesso")


def search(products):
    """


    :param products:
    :return:
    """
    pesq = input("Qual camiseta deseja pesquisar: ")
    if pesq not in products:
        print("Camiseta não encontrada")
    else:
        print(products[pesq])


def get_str_value(message: str):
    """
    Valida dados informados pelo usuário

    :param message: Mensagem do input exibida ao usuário
    :return palavra: Valor escrito informado pelo usuário
    """
    while True:
        try:
            palavra = str(input(message))
            return palavra
        except ValueError:
            print('Digite uma palavra! ')


# Editando os produtos
def edit(products):
    """


    :param products:
    :return:
    """
    print("-=" * 30)
    name = input("Qual produto deseja editar: ")
    while True:
        if name not in products:
            print("Produto não encontrado.")
            name = input("Qual produto deseja editar: ")
        else:
            break
    size = input("Tamanho da camiseta [P/M/G/GG]: ").upper()[0]
    while True:
        if size == "P" or size == "M" or size == "G":
            break
        else:
            print("Tamanho invalido")
            size = input("Tamanho da camiseta [P/M/G/GG]: ").upper()[0]
    quantidade = input("Qual a quantidade no estoque: ")
    preco = input("Qual o preco: ")
    products[name] = {CONST_NAME_SIZE: size,
                     CONST_NAME_QUANTITY: quantidade,
                     CONST_NAME_PRICE: preco}


# Adicionando produtos
def add_product(products):
    name = get_str_value('Digite o time de futebol: ').strip()
    size = input("Tamanho da camiseta [P/M/G/GG]: ").upper()
    quantity = int(input("Quantidade no estoque: "))
    price = float(input("Preco da camiseta: "))
    products[name] = {CONST_NAME_SIZE: size,
                      CONST_NAME_QUANTITY: quantity,
                      CONST_NAME_PRICE: price}


# Criando um menu
def menu():
    """


    :return:
    """
    print("=== Cadastro de produtos ===")
    print("1- Cadastrar produto")
    print("2- Alterar produto")
    print("3- Pesquisar produto")
    print("4- Mostrar o produto")
    print("5- Remover produto")
    print("6- Sair")
    return get_int_value_with_range("O que deseja fazer", 1, 6)


def save_in_file_dict(produtos: str, products: dict):
    """
    Salvar um dicionário em um arquivo binário.

    :param produtos: Nome do Arquivo.
    :param products: Nome do Dicionário.
    """
    with open(produtos, "wb") as f:
        pickle.dump(products, f)


# Criando funçao main
def main():
    """


    :return:
    """
    products = {}
    while True:
        op = menu()
        if op == 1:
            add_product(products)
        elif op == 2:
            edit(products)
        elif op == 3:
            search(products)
        elif op == 4:
            print(products)
        elif op == 5:
            remove(products)
        elif op == 6:
            print("-=" * 30)
            print("=== VOLTE SEMRE ===")
            break


if __name__ == '__main__':
    main()
