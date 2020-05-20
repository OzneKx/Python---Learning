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


#Keys do dicionário
CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


#Exibe o menu de opções
def menu():
    print('=-= Sistema de Cadastro de Clientes =-=')
    print('[1] Cadastrar Cliente\n'
          '[2] Alterar dados de cliente\n'
          '[3] Excluir cliente\n'
          '[4] Pesquisar Cliente\n'
          '[5] Zerar Banco de Dados\n'
          '[6] SAIR')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    return get_int_value_with_range("Digite uma das opções", 1, 6)


#Validando dados inteiros em um determinado range
def get_int_value_with_range(message, min_value, max_value):
    while True:
        try:
            escolha = int(input(f'{message}: '))
        except ValueError:
            print("Formato inválido: esperado um número")
            continue
        if not min_value <= escolha <= max_value:
            print(f'Opção inválida: escolha um número de {min_value} a {max_value}')
        else:
            return escolha


#Cadastra clientes
def client_register(clients):
    id = input('Informe o CPF do cliente: ')
    name = input('Informe o nome do cliente: ')
    city = input('Informe a cidade do cliente: ')
    age = get_int_value_with_range("Digite a idade do cliente", 18, 120)
    if id in clients:
        return False
    else:
        clients[id] = {
            CONST_FIELD_NAME: name,
            CONST_FIELD_CITY: city,
            CONST_FIELD_AGE: age
        }
        print('Cliente cadastrado com sucesso! ')
        return True


#Edita os dados de clientes
def client_edit(clients):
    editar = int(input('[1] Nome\n'
                       '[2] Cidade\n'
                       '[3] Idade\n'
                       'Faça sua escolha: '))
    if editar == 1: 
        clients['name'] = input('Nome substituto: ')
    elif editar == 2:
        clients['city'] = input('Cidade substituta: ')
    else:
        clients['age'] = input('Idade substituta: ')


#Remove clientes
def client_del(clients):
    cpf = input('Informe o cpf do cliente que deseja remover: ')         #Remoção do cliente através do CPF
    if cpf == id:
        for v in clients.values():
            clients.pop(v)


#Pesquisa clientes
def client_query(clients):
    buscar = input('Informe o cpf do cliente que deseja pesquisar: ')     #Pesquisa do cliente através do CPF
    if buscar in clients:
        clients[buscar]
    print(clients[buscar])


#Exclui o banco de dados
def database_clear(clients):
    really = int(input('Certeza de que gostaria de deletar o banco de dados?\n'    #Confirmar se deseja mesmo deletar o banco de dados
                       '[1] SIM\n'
                       '[2] NÃO\n'
                       'Escolha: '))
    if really == 1:
        clients.clear()
    else:
        print('O banco de dados não foi deletado! ')


#Ponto de entrada do módulo
def main():
    clients = {}                                    #Banco de dados no formato dicionário
    while True:
        escolha = menu()
        if escolha == 1:
            if client_register(clients):
                print('Cliente cadastrado com sucesso! ')
            else:
                print('Problemas no cadastro do cliente! ')
        elif escolha == 2:
            if client_edit(clients):
                print('Dados alterados com sucesso! ')
            else:
                print('Problemas na alteração de dados do cliente! ')
        elif escolha == 3:
            if client_del(clients):
                print('Cliente exluido com sucesso ')
            else:
                print('Problemas na exclusão do cliente! ')
        elif escolha == 4:
            if client_query(clients):
                print('Cliente encontrado com sucesso! ')
        elif escolha == 5:
            if database_clear(clients):
                print('Banco de dados limpo com sucesso! ')
            else:
                print('Problemas ao deletar o banco de dados! ')
        elif escolha == 6: 
            print('Volte sempre! ')                              #Saída do programa com mensagem de agradecimento ao usuário
            break


#Modularização
if __name__ == '__main__':
    main()
