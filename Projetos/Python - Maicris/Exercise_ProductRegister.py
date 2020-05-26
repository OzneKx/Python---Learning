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


def menu():
  ornament('Cadastro de Produtos')
  ornament_two('SUAS OPÇÕES')
  print('[1] Cadastrar Produto\n'
        '[2] Alterar Produto\n'
        '[3] Pesquisar Produto\n'
        '[4] Listar Produtos\n'
        '[5] Remover Estoque\n'
        '[6] SAIR')
  return get_int_value_with_range('Digite uma das opções: ', 1, 6) 


def get_int_value_with_range(message: str, min_value: int, max_value: int) -> int:
  """
  Valida dados inteiros em um determinado range

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


def yes_or_no_value(message):
  """
  Exibe mensagem de confirmação na tentativa de remoção do estoque

  :param message: 


  """
  while True:
    escolha = input(f'{message}: ')
    if escolha in 'SN':
      return escolha
    else:
      print('Inválido! Escolha [S] sim ou [N] [não]' )
