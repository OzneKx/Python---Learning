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
            print("Opção inválida: escolha um número de", min_value, "a", max_value)
        else:
            return op

def get_yes_no_value(message):
    while True:
        op = input(message + ": ")
        if op == 's' or op == 'n':
            return op
        else:
            print("Opção inválida: escolha s (sim) ou n (não)")


# Realiza inclusão / edição de dados do cliente
def register_client(id, clients):
    name = input("Por favor, digite o nome do cliente: ")
    city = input("Por favor, digite a cidade do cliente: ")
    age = get_int_value_with_range("Digite a idade do cliente", 18, 120)
    clients[id] = {
        CONST_FIELD_NAME: name,
        CONST_FIELD_CITY: city,
        CONST_FIELD_AGE: age
    }


# Apaga o banco de dados
def database_clear(clients):
    op = get_yes_no_value("Tem certeza que deseja zerar o banco de dados")
    if op == 's':
        clients.clear()
        return True, "Dados zerados com sucesso"
    else:
        return False, "Operação cancelada pelo usuário"


# Pesquisa clientes
def client_query(clients):
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        print("Nome do cliente:", clients[id][CONST_FIELD_NAME])
        print("Cidade do cliente:", clients[id][CONST_FIELD_CITY])
        print("Idade do cliente:", clients[id][CONST_FIELD_AGE])
        input("")
    else:
        print("Cliente não localizado")
        input("")


# Exclui clientes
def client_del(clients):
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        op = get_yes_no_value("Tem certeza que deseja excluir este cliente")
        if op == 's':
            del clients[id]
            return True, "Cliente excluído com sucesso"
        else:
            return False, "Operação cancelada pelo usuário"


# Edita os dados de clientes
def client_edit(clients):
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        register_client(id, clients)
        return True, "Cliente alterado com sucesso"
    else:
        op = get_yes_no_value("Cliente não localizado. Deseja fazer seu cadastro")
        if op == 's':
            register_client(id, clients)
            return True, "Cliente cadastrado com sucesso"
        else:
            return False, "Cliente não localizado."


# Cadastra clientes
def client_add(clients):
    id = input("Por favor, digite o CPF do cliente: ")
    if id in clients:
        op = get_yes_no_value("Cliente já existente. Deseja alterar seus dados")
        if op == 's':
            register_client(id, clients)
            return True, "Cliente alterado com sucesso"
        else:
            return False, "Cadastro não realizado. Cliente já existente"
    else:
        register_client(id, clients)
        return True, "Cliente cadastrado com sucesso"


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
            resp, msg = client_add(clients)
            print(msg)
            input("")

        elif op == 2:
            resp, msg = client_edit(clients)
            print(msg)
            input("")

        elif op == 3:
            resp, msg = client_del(clients)
            print(msg)
            input("")

        elif op == 4:
            client_query(clients)

        elif op == 5:
            resp, msg = database_clear(clients)
            print(msg)
            if resp:
                r = get_yes_no_value("Deseja criar um primeiro cliente")
                if r == 's':
                    client_add(clients)

        elif op == 6:
            break


if __name__ == '__main__':
    main()
