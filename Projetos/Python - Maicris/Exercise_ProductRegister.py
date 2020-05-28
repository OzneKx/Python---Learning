"""
Atividade Somativa - Raciocínio Algorítmico
Cadastro de produtos num banco de dados

guitarras {
  serie: {
    Modelo: ,
    Marca: ,
    Ano: ,
    País: ,
    Description: ,
  }
}
"""

from datetime import date

CONST_FIELD_MODEL = "Modelo"
CONST_FIELD_BRAND = "Marca"
CONST_FIELD_YEAR = "Ano de Fabricação"
CONST_FIELD_COUNTRY = "Origem de Fabricação"
CONST_FIELD_COST = "Custo"
CONST_FIELD_DESCRIPTION = "Descrição"


def ornament(txt: str):
  """
  Enfeite de textos, de acordo com teu tamanho

  :param txt: Texto a ser exibido
  """
  print('~' * len(txt))
  print(txt)
  print('~' * len(txt))


def ornament_two(text: str):
  """
  Outro enfeite de textos, de acordo com teu tamanho

  :param txt: Texto a ser exibido
  """
  print('-' * len(text))
  print(text)
  print('-' * len(text))  


def actual_time():
  """
  Importa a função date da library do Python

  :param date: Identifica o ano atual
  :return: Retorna a data do ano atual 
  """
  atual = date.today().year
  return atual


def menu():
  ornament('Cadastro de Guitarras')
  ornament_two('SUAS OPÇÕES')
  print('[1] Cadastrar Guitarras\n'
        '[2] Alterar Guitarras\n'
        '[3] Pesquisar Guitarras\n'
        '[4] Listar Guitarras\n'
        '[5] Remover Estoque\n'
        '[6] SAIR')
  return get_int_value_with_range('Digite uma das opções: ', 1, 6) 


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
      escolha = int(input(f'{message}').strip())
    except ValueError:
      print('Formato inválido! Digite um NÚMERO!')
      continue
    if not min_value <= escolha <= max_value:
      print(f'Opção inválida! Sua escolha deve ser entre {min_value} e {max_value}...')
    else: 
      return escolha


def yes_or_no_value(message: str):
  """
  Exibe mensagem de confirmação na tentativa de remoção do estoque

  :param message: Mensagem exibida ao usuário antes de remover o estoque
  :return: Retorna a escolha feita pelo usuário
  """
  while True:
    escolha = input(f'{message}: ').strip().upper()[0]
    if escolha in 'SN':
      return escolha
    else:
      print('Inválido! Escolha [S] - sim ou [N] - não' )


def guitar_register(serie: int, guitarras) -> int:
  """
  Registrar guitarra e suas especificações
  
  :param guitarras: Número de série de produção da guitarra
  :param guitarra: Características da guitarra ao cadastrá-la
  """
  model = input('Modelo da guitarra: ').capitalize().strip()
  brand = input('Fabricante da guitarra: ').capitalize().strip()
  year = get_int_value_with_range('Ano de fabricação: ', 1931, actual_time())
  country = input('Origem da fabricação da guitarra: ').capitalize().strip()
  cost = input('Valor do produto: R$').strip()
  description = input('Descrição da guitarra: ').capitalize().strip()
  guitarras[serie] = {
    CONST_FIELD_MODEL: model,
    CONST_FIELD_BRAND: brand,
    CONST_FIELD_YEAR: year,
    CONST_FIELD_COUNTRY: country,
    CONST_FIELD_COST: cost,
    CONST_FIELD_DESCRIPTION: description
  }


def guitar_edit(guitarras):
  """
  Altera dados dos registros da guitarra

  :param guitarras: Exibe os dados dos registros de guitarras
  :return: Mensagem da condição da alteração de dados da guitarra
  """
  serie = input('Número de série da guitarra: ')
  if serie in guitarras:
    guitar_register(serie, guitarras)
    return True, "Especificações da guitarra alteradas com sucesso! "
  else:
    escolha = yes_or_no_value("Guitarra não localizada. Deseja cadastra-la?").strip().upper()[0]
    if escolha == "S":
      guitar_register(serie, guitarras)
      return True, "Guitarra cadastrada com sucesso! "
    else: 
      return False, "Guitarra não localizada! "


def search_guitar(guitarras):
  """
  Procura guitarras no banco de dados

  :param guitarras: Possibilita a pesquisa de guitarras registradas
  """
  serie = input('Número de série da guitarra: ').strip()
  if serie in guitarras:
    print('Modelo da guitarra: ', guitarras[serie][CONST_FIELD_MODEL])
    print('Marca da guitarra: ', guitarras[serie][CONST_FIELD_BRAND])
    print('Ano de fabricação da guitarra: ', guitarras[serie][CONST_FIELD_YEAR])
    print('Origem de fabricação da guitarra: ', guitarras[serie][CONST_FIELD_COUNTRY])
    print('Custo da guitarra: ', guitarras[serie][CONST_FIELD_COST])
    print('Descrição da guitarra: ', guitarras[serie][CONST_FIELD_DESCRIPTION])
  else: 
    print('Guitarra não localizada ')


def list_guitar(guitarra):
  """
  Lista as guitarras contidas no dicionário

  :param guitarra: Exibe as guitarras registradas no dicionário
  """
  for k, v in guitarra.items():
    print(f'{k} : {v}')


def stockpile_remove(guitarras):
  """
  Remoção de guitarras do estoque

  :param guitarra: Identifica guitarras no estoque a serem removidos
  """
  serie = input('Digite o número de série da guitarra: ').strip()
  if serie in guitarras:
    escolha = yes_or_no_value('Certeza que deseja remover a guitarra do estoque').strip().upper()[0]
    if escolha == 'S':
      del guitarras[serie]
      return True, 'Guitarra removida do estoque com sucesso! '
    else:
      return False, 'Nenhuma guitarra foi removida do estoque! '


def main():
  serie = 0
  guitarras = {}
  while True:
    escolha = menu()
    if escolha == 1:
      guitar_register(serie, guitarras)
    if escolha == 2:
      guitar_edit(guitarras)
    if escolha == 3:
      search_guitar(guitarras)
    if escolha == 4:
      list_guitar(guitarras)
    if escolha == 5:
      stockpile_remove(guitarras)
    if escolha == 6:
      break


if __name__ == '__main__':
  main()