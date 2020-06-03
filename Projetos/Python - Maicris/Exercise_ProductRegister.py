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
  :return: None
  """
  print('~' * len(txt))
  print(txt)
  print('~' * len(txt))


def ornament_two(text: str):
  """
  Outro enfeite de textos, de acordo com teu tamanho

  :param txt: Texto a ser exibido
  :return: None
  """
  print('=' * len(text))
  print(text)
  print('=' * len(text))  


def actual_time():
  """
  Importa a função date da library do Python

  :return: Retorna a data do ano atual 
  """
  atual = date.today().year
  return atual


def sleep():
  """
  Importa a função sleep da library do Python
  :return: None
  """
  from time import sleep                             
  sleep(1.5)


def menu():
  ornament('Cadastro de Guitarras')
  ornament_two('-----SUAS OPÇÕES-----')
  print('[1] Cadastrar Guitarras\n'
        '[2] Alterar Guitarras\n'
        '[3] Pesquisar Guitarras\n'
        '[4] Listar Guitarras\n'
        '[5] Remover Estoque\n'
        '[6] SAIR')
  print('=' * 23)
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
  :return: None
  """
  serie = input('Informe o número de série da guitarra: ')
  model = input('Modelo da guitarra: \n'
                ' -> SG\n'
                ' -> Les Paul\n'
                ' -> Explorer\n'
                ' -> Flying V\n'
                ' -> Telecaster\n'
                ' -> Stratocaster\n'
                'Escolha: ').capitalize().strip()
  brand = input('Fabricante da guitarra: \n'
                ' -> Gibson\n'
                ' -> Fender\n'
                ' -> Ibanez\n'
                ' -> Yamaha\n'
                ' -> Epiphone\n'
                'Escolha (Se for outra, digite aqui): ').capitalize().strip()
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
  :return: None
  """
  serie = input('Número de série da guitarra: ')
  if serie in guitarras:
    guitar_register(serie, guitarras)
    return True, "Especificações da guitarra alteradas com sucesso! "
  else:
    escolha = yes_or_no_value("Guitarra não localizada. Deseja cadastrá-la?").strip().upper()[0]
    if escolha == "S":
      guitar_register(serie, guitarras)
      print('Guitarra cadastrada com sucesso! ')
    else: 
      print('Guitarra não localizada! ')


def search_guitar(guitarras):
  """
  Procura guitarras no banco de dados

  :param guitarras: Possibilita a pesquisa de guitarras registradas
  :return: None
  """
  serie = input('Número de série da guitarra: ').strip()
  if serie in guitarras:
    print(f'Modelo da guitarra: {guitarras[serie][CONST_FIELD_MODEL]}')
    print(f'Marca da guitarra: {guitarras[serie][CONST_FIELD_BRAND]}')
    print(f'Ano de fabricação da guitarra: {guitarras[serie][CONST_FIELD_YEAR]} ')
    print(f'Origem de fabricação da guitarra: {guitarras[serie][CONST_FIELD_COUNTRY]} ')
    print(f'Custo da guitarra: {guitarras[serie][CONST_FIELD_COST]} ')
    print(f'Descrição da guitarra: {guitarras[serie][CONST_FIELD_DESCRIPTION]} ')
    sleep()
  else: 
    escolha = yes_or_no_value("Guitarra não localizada. Deseja cadastrá-la? [S/N]").strip().upper()[0]
    if escolha == "S":
      guitar_register(serie, guitarras)
      print('Guitarra cadastrada com sucesso! ')
    else: 
      print('Guitarra não localizada! ')


def list_guitar(guitarra):
  """
  Lista as guitarras contidas no dicionário

  :param guitarra: Exibe as guitarras registradas no dicionário
  :return: None
  """
  for k, v in guitarra.items():
    print(f'Número de série da guitarra e suas características -> {k} : {v}')
  sleep()


def stockpile_remove(guitarras):
  """
  Remoção de guitarras do estoque

  :param guitarra: Identifica guitarras no estoque a serem removidos
  :return: None
  """
  serie = input('Digite o número de série da guitarra: ').strip()
  if serie in guitarras:
    escolha = yes_or_no_value('Certeza que deseja remover a guitarra do estoque [S/N]: ').strip().upper()[0]
    if escolha == 'S':
      del guitarras[serie]
      print('Guitarra removida do estoque com sucesso! ')
    else:
      print('Nenhuma guitarra foi removida do estoque! ')


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
      sair = yes_or_no_value('Certeza de que deseja sair do programa? [S/N]').strip().upper()[0]
      if sair == 'S': 
        print('Volte sempre! ')
        break
      else:
        print('Você optou por não sair do programa! ')
        sleep()


if __name__ == '__main__':
  main()