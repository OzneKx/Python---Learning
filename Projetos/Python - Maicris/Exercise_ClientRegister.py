"""
Exemplo de uso de funções para cadastro
Uso de Dicionários como banco de dados
Estrutura:

clients {
    id : {
        name: ,
        city: ,
        age:
    }
}
"""

CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


# Validando dados inteiros em um determinado range
def get_int_value_with_range(message, min_value, max_value):
    while True:
        try:
            op = int(input(message + ": "))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= op <= max_value:
            print("Opção inválida: escolha um número de",
                  min_value, "a", max_value)
        else:
            return op

            
# Apaga o banco de dados
def database_clear():
    pass


# Pesquisa clientes
def client_query():
    pass


# Exclui clientes
def client_del():
    pass


# Edita os dados de clientes
def client_edit():
    pass


# Cadastra clientes
def client_add(clients):
    id = input("Por favor, digite o CPF do cliente: ")
    name = input("Por favor, digite o nome do cliente: ")
    city = input("Por favor, digite a cidade do cliente: ")
    age = get_int_value_with_range("Digite a idade do cliente", 18, 120)
    if id in clients:
        return False
    else:
        clients[id] = {
            CONST_FIELD_NAME: name,
            CONST_FIELD_CITY: city,
            CONST_FIELD_AGE: age
        }
        return True


# Exibe o menu de opções
def menu():
    print("*** Sistema de Cadastro de Clientes ***")
    print("1. Cadastrar cliente")
    print("2. Alterar dados de cliente")
    print("3. Excluir cliente")
    print("4. Pesquisar cliente")
    print("5. Zerar banco de dados")
    print("6. Sair")
    print("***************************************\n")
    return get_int_value_with_range("Digite uma das opções", 1, 6)


# Ponto de entrada do módulo
def main():
    clients = {}  # banco de dados no formato dicionário
    while True:
        op = menu()
        if op == 1:
            if client_add(clients):
                "Cliente cadastrado com sucesso"
            else:
                "Problemas no cadastro do cliente"
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            break


if __name__ == '__main__':
    main()
