"""
Atividade Somativa - Raciocínio Algorítmico
Cadastro de produtos num banco de dados
"""


def ornament(txt):
  """
  Enfeite de textos, de acordo com teu tamanho

  :param txt: Texto a ser exibido
  """
  print('~' * len(txt))
  print(txt)
  print('~' * len(txt))


def ornament_two(text):
  """
  Outro enfeite de textos, de acordo com teu tamanho

  :param txt: Texto a ser exibido
  """
  print('-' * len(text))
  print(text)
  print('-' * len(text))  


def actual_time(date):
  """
  Importa a função date da library do Python

  :param date: Exibe o ano atual

  """
  from datetime import dat
  atual = date.today().year


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
      escolha = int(input(f'{message}: '))
    except ValueError:
      print('Formato inválido! Digite um NÚMERO!')
      continue
    if not min_value <= escolha <= max_value:
      print(f'Opção inválida! Sua escolha deve ser entre {min_value} e {max_value}...')
    else: return escolha


def yes_or_no_value(guitarras):
  """
  Exibe mensagem de confirmação na tentativa de remoção do estoque

  :param message: Mensagem exibida ao usuário antes de remover o estoque
  :return: Retorna a escolha feita pelo usuário
  """
  while True:
    escolha = input(f'{message}: ')
    if escolha in 'SN':
      return escolha
    else:
      print('Inválido! Escolha [S] - sim ou [N] - não' )


def guitar_register(guitarras):
  """
  Registrar guitarra e suas especificações

  :param guitarra: Características da guitarra ao cadastrá-la
  """
  model = input('Modelo da guitarra: ')
  brand = input('Fabricante da guitarra: ')
  year =get_int_value_with_range('Ano de fabricação: ', 1931, )



def stockpile_remove(guitarras):
  """
  Remoção de guitarras do estoque a

  :param guitarra: Identifica guitarras no estoque a serem removidos
  """


def main():
  guitarras = {}
  while True:
    escolha = menu():
    if escolha == 1:

    if escolha == 2:

    if escolha == 3:

    if escolha == 4:

    if escolha == 5:

    if escolha == 6:

