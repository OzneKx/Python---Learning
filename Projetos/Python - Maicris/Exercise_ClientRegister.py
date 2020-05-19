"""
Exemplo de uso de funções para cadastro
Uso de Dicionários como banco de dados
Estrutura:

clients {
    id: {
        name: ,
        city: ,
        age:
    }
}
"""

CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


# Limpa o banco de dados
def database_clear():
    pass


# Pesquisa Clientes
def client_query():
    pass


# Deleta clientes
def client_del():
    pass


# Edita os dados dos clientes
def client_edit():
    pass


# Edita os dados de clientes
def client_register(clients):
    id = input('Informe o CPF do cliente: ')
    name = input('Informe o nome do cliente: ')
    city = input('Informe a cidade do cliente: ')
    age = get_int_value_with_range(f'Digite a idade do cliente {18} {120}')
    if id in clients:
        return False
    else:
        clients[id] = {
            CONST_FIELD_NAME: name,
            CONST_FIELD_CITY: city,
            CONST_FIELD_AGE: age
        }
        return True


# Validando dados inteiros em um determinado range
def get_int_value_with_range(message, min_value, max_value):
    while True:
        try:
            escolha = int(input(f'{message}: '))
        except ValueError:
            print('Formato inválido: esperado número')
            continue
        if not min_value <= escolha <= max_value:
            print(
                f'Opção inválida: escolha um número de {min_value} a {max_value}')
        else:
            return escolha

            
# Exibe o menu de opções
def menu():
    print('Sistema de Cadastro de Clientes')
    print('[1] Cadastrar Cliente\n'
          '[2] Alterar dados de cliente\n'
          '[3] Excluir clientez\n'
          '[4] Pesquisar Cliente\n'
          '[5] Zerar Banco de Dados\n'
          '[6] SAIR')
    return get_int_value_with_range(f'Digite uma das opções: {1} a {6}')


# Ponto de entrada do módulo
def main():
    clients = {}  # Banco de dados no formato dicionário
    while True:
        escolha = menu()
        if escolha == 1:
            if client_register(clients):
                "Cliente cadastrado com sucesso"
            else:
                "Problemas ao cadastrar o cliente"
        elif escolha == 2:

        elif escolha == 3:
            pass
        elif escolha == 3:
            pass
        elif escolha == 4:
            pass
        elif escolha == 5:
            pass
        elif escolha == 6:
            break


if __name__ == '__main__':
    main()
