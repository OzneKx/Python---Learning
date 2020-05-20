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

#
def sleep():
    from time import sleep   #Importando sleep do time
    sleep(1)


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
    editar = input('Informe o cpf do cliente a ser editado: ')
    if editar in clients:
        new_data = input('Deseja mesmo alterar? [S/N]: ').upper()
        if new_data == 'S':
            clients.pop(editar)
            client_register(clients)
        elif new_data == 'N':
            print('Não houveram aterações de dados do cliente... ')
     

#Remove clientes
def client_del(clients):
    remover = input('Informe o cpf do cliente que deseja remover: ')      #Remoção do cliente através do CPF
    if remover == clients:
        clients.pop(remover)
        print('Cliente removido com sucesso! ')
    else:
        print('Cliente não encontrado. Não foi possível removê-lo... ')


#Pesquisa clientes
def client_query(clients):
    buscar = input('Informe o cpf do cliente que deseja pesquisar: ')     #Pesquisa do cliente através do CPF
    if buscar in clients:
        clients[buscar]
        print('Cliente encontrado: ')
        print(clients[buscar])
    else:
        print('Não foi possível encontrar o cliente... ')


#Exclui o banco de dados
def database_clear(clients):
    really = input('Certeza de que gostaria de deletar o banco de dados\n'    #Confirmar se deseja mesmo deletar o banco de dados
                       '[S] SIM\n'
                       '[N] NÃO\n'
                       'Escolha: ').upper()
    if really == 'S':
        clients.clear()
        print('Banco de dados deletado com sucesso! ')
    elif really == 'N':
        print('O banco de dados não foi deletado... ')


#Ponto de entrada do módulo
def main():
    clients = {}                                     #Banco de dados no formato dicionário
    while True:
        escolha = menu()
        if escolha == 1:
            client_register(clients)
        elif escolha == 2:
            client_edit(clients)
        elif escolha == 3:
            client_del(clients)
        elif escolha == 4:
            client_query(clients)
        elif escolha == 5:
            database_clear(clients)
        elif escolha == 6: 
            print('Volte sempre! ')                              #Saída do programa com mensagem de agradecimento ao usuário
            break


#Modularização
if __name__ == '__main__':
    main()
