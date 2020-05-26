"""
Exemplo de uso de funções para cadastro
Uso de Dicionários como banco de dados
Estrutura:

#Dados de cadastro do cliente
clients {
    id : {
        name: nome do usuário,
        city: cidade do usuário ,
        age:  idade do usuário
    }
}
"""


#Definindo uma função para o uso do sleep
def sleep():
    from time import sleep                              #Importando sleep do time
    sleep(1.5)


#Keys do dicionário
CONST_FIELD_NAME = "name"
CONST_FIELD_CITY = "city"
CONST_FIELD_AGE = "age"


#Exibe o menu de opções
def menu():
    print('Processando...')
    sleep()
    print('\033[31m=-=\033[m' * 10)
    print(f'\033[33m{"CADASTRAR CLIENTES":^30}\033[m')
    print('\033[31m=-=\033[m' * 10)
    print('---------SUAS OPÇÕES----------')                             #Exibição do menu
    print('\033[34m[1] Cadastrar Cliente\n'
          '[2] Alterar dados de cliente\n'
          '[3] Excluir cliente\n'
          '[4] Pesquisar Cliente\n'
          '[5] Zerar Banco de Dados\n'
          '[6] SAIR\033[m')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    return get_int_value_with_range("Digite uma das opções: ", 1, 6)     #Solicitar ao usuário digitar corretamente as opções disponíveis


#Validando dados inteiros em um determinado range
def get_int_value_with_range(message, min_value, max_value):
    while True:
        try:
            escolha = int(input(f'{message}: '))
        except ValueError:
            print("\033[31mFormato inválido: esperado um número\033[m")     #Mensagem de formato inválido quando uma letra for inserida no lugar de um número
            continue
        if not min_value <= escolha <= max_value:
            print(f'\033[31mOpção inválida: escolha um número de {min_value} a {max_value}\033[m')  #Mensagem de formato inválido quando um número fora das opções forem inseridos
        else:
            return escolha


#Cadastro de clientes
def client_register(clients):                           #Solicitar ao usuário dados básicos para o cadastro
    id = input('Informe a identidade do cliente: ')
    name = input('Informe o nome do cliente: ')
    city = input('Informe a cidade do cliente: ')
    age = get_int_value_with_range("Digite a idade do cliente\033", 18, 120)
    if id in clients:
        return False
    else:
        clients[id] = {
            CONST_FIELD_NAME: name,
            CONST_FIELD_CITY: city,
            CONST_FIELD_AGE: age
        }
        print('\033[33mCliente cadastrado com sucesso! \033[m')                 #Mensagem de sucesso em cadastrar o cliente
        return True


#Edita os dados de clientes
def client_edit(clients):
    editar = input('Informe a identidade do cliente a ser editado: ')           #Solicitar a identidade do cliente para que seja possível editá-lo
    if editar in clients:
        new_data = input('Deseja mesmo alterar? [S/N]: ').upper()               #Confirmar se o usuário deseja realizar ou não uma alteração do cliente
        if new_data == 'S':
            clients.pop(editar)
            client_register(clients)
            print('\033[33mDados do cliente alterados com sucesso! \033[m')     #Mensagem de sucesso ao alterar os dados do cliente
            sleep()
        elif new_data == 'N':
            print('\033[31mNão houveram aterações de dados do cliente...\033[m ')  #Mensagem de erro em alterar os dados o cliente
            sleep()


#Remove clientes
def client_del(clients):
    remover = input('Informe a identidade do cliente que deseja remover: ')      #Remoção do cliente através do CPF
    if remover == clients:
        clients.pop(remover)
        print('\033[33mCliente removido com sucesso! \033[m')                    #Mensagem de sucesso em remover o cliente
        sleep()
    else:
        print('\033[31mCliente não encontrado. Não foi possível removê-lo... \033[m')   #Mensagem de erro em encontrar o cliente
        sleep()


#Pesquisa clientes
def client_query(clients):
    buscar = input('Informe a identidade do cliente que deseja pesquisar: ')     #Pesquisa do cliente através de sua identidade
    if buscar in clients:
        clients[buscar]
        print('Cliente encontrado: ')                                            #Mensagem de sucesso em encontrar o cliente
        print(clients[buscar])
        sleep()
    else:
        print('\033[31mNão foi possível encontrar o cliente... \033[m')          #Mensagem de erro em encontrar o cliente
        sleep()


#Exclui o banco de dados
def database_clear(clients):
    really = input('Certeza de que gostaria de deletar o banco de dados\n'       #Confirmar se deseja mesmo deletar o banco de dados
                       '[S] SIM\n'
                       '[N] NÃO\n'
                       'Escolha: ').upper()
    if really == 'S':
        clients.clear()
        print('\033[33mBanco de dados deletado com sucesso! \033[m')            #Mensagem de sucesso em limpar o banco de dados
        sleep()
    elif really == 'N':
        print('\033[31mO banco de dados não foi deletado...\033[m ')            #Mensagem de erro em limpar o banco de dados
        sleep()


#Ponto de entrada do módulo
def main():
    clients = {}                                                                #Banco de dados no formato dicionário
    while True:
        escolha = menu()
        if escolha == 1:
            client_register(clients)                                            #Chamar a função
        elif escolha == 2:
            client_edit(clients)                                                #Chamar a função
        elif escolha == 3:
            client_del(clients)                                                 #Chamar a função
        elif escolha == 4:
            client_query(clients)                                               #Chamar a função
        elif escolha == 5:
            database_clear(clients)                                             #Chamar a função
        elif escolha == 6:
            sleep() 
            print('\033[33mVolte sempre! \033[m ')                              #Saída do programa com mensagem de agradecimento ao usuário
            break


#Modularização
if __name__ == '__main__':
    main()
