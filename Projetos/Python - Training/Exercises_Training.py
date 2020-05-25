'''dict_alunos = {}
dict_alunos["Nome"] = str(input('Nome do aluno: '))
media = float(input('Média do aluno: '))
dict_alunos["Média"] = media
if media <= 5:
  dict_alunos["Situação"] = 'Reprovado'
elif 5 < media < 7:
  dict_alunos["Situação"] = 'Recuperação'
elif media >= 7:
  dict_alunos["Situação"] = 'Aprovado'
for k, v in dict_alunos.items():
  print(f'{k} = {v}')'''


'''from operator import itemgetter
dict_dice = {}
from random import randint
for c in range(1, 4 + 1, 1):
  dict_dice[c] = randint(1, 7)
  print(f'O jogador {c} tirou {dict_dice[c]}')
print('---------RANKING FINAL---------')
maior = 0
for k, v in sorted(dict_dice.items(), key=itemgetter(1), reverse=True):
  maior += 1
  print(f'{k} ficou em {maior}° lugar, com: {v} pontos. ')'''


'''from datetime import date
dict_cadastro = {}
ano_atual = date.today().year
dict_cadastro["Nome"] = str(input('Digite seu nome: '))
nascimento = int(input('Ano de nascimento: '))
dict_cadastro["Idade"] = (ano_atual - nascimento)
dict_cadastro["CTPS"] = int(input('Carteira de trabalho (0 NÃO TEM): '))
if dict_cadastro["CTPS"] != 0:
  dict_cadastro["Ano de Contratação"] = int(input('Ano de contratação: '))
  dict_cadastro["Salário"] = float(input('Salário: R$'))
  dict_cadastro["Aposentadoria"] = ((dict_cadastro["Ano de Contratação"] + 35) +  dict_cadastro["Idade"] - ano_atual)
for k, v in dict_cadastro.items():
  print(f'{k} tem valor igual a = {v}')'''

    
'''dict_fut = {}
dict_fut["Nome"] = str(input('Nome do jogador: '))
dict_fut["Partidas"] = int(input('Total de partidas jogadas por ele: '))
dict_fut["Gols"] = []
for c in range(1, dict_fut["Partidas"] + 1):
  dict_fut["Gols"].append(int(input(f'Números de gols na {c}ª partida: ')))
dict_fut["Total"] = sum(dict_fut["Gols"]) 
print('=-=' * 20)
print(f'O jogador {dict_fut["Nome"]} jogou {dict_fut["Partidas"]} partidas. ') 
for x in range(0, dict_fut["Partidas"]):
  print(f'Na {x + 1}ª partida, {dict_fut["Gols"][x]} gols.')
print(f'O total de gols, entretanto, foi de: {dict_fut["Total"]}')'''


''''dict_pessoas = {}
lista_pessoas = []
soma = 0
while True:
  dict_pessoas.clear()
  dict_pessoas["Nome"] = str(input('Seu nome: '))
  while True:
    dict_pessoas["Sexo"] = str(input('Seu Sexo: [M/F]: ')).strip().upper()[0]
    if dict_pessoas["Sexo"] in "MF":
      break
    print('Digite apenas M ou F! ')
  dict_pessoas["Idade"] = int(input('Sua idade: '))
  soma += dict_pessoas["Idade"]
  lista_pessoas.append(dict_pessoas.copy())
  while True:
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar in 'S/N': 
      break
    print('Responda apenas [S] ou [N]! ')
  if continuar == 'N': 
    break
media_idade = soma / len(lista_pessoas)
print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')
print(f'A média de idade do grupo é igual a {media_idade}')
print('Lista de mulheres: ', end='')
for c in lista_pessoas:
  if c["Sexo"] == 'F':
    print(f'{c["Nome"]} ', end='')
print()
print('Pessoas com idade superior a média: ')
for c in lista_pessoas:
  if c["Idade"] >= media_idade:
    for k, v in c.items():
      print(f'{k} = {v}; ', end='')
    print()
print('ACABOU')'''


'''dict_fut = {}
lista_fut = []
lista_partidas = []
while True:
  dict_fut.clear()
  dict_fut["Nome"] = str(input('Nome do jogador: ')).capitalize()
  total = int(input('Total de partidas jogadas por ele: '))
  lista_partidas.clear()
  for c in range(0, total):
    lista_partidas.append(int(input(f'Números de gols na {c + 1}ª partida: ')))
  dict_fut["Gols"] = lista_partidas[:]
  dict_fut["Total"] = sum(lista_partidas)
  lista_fut.append(dict_fut.copy()) 
  while True:
    continuar = input('Continuar? [S/N]: ').strip().upper()[0]
    if continuar in "SN":
      break
    print('Responda com [S] ou [N]! ')
  if continuar == 'N':
    break
print('=-=' * 20)
print('cod', end='')
for i in dict_fut.keys():
  print(f'{i:<15}', end='')
print()
print('=-=' * 20)
for k, v in enumerate(lista_fut):
  print(f'{k:>4} ', end='')
  for d in v.values():
    print(f'{str(d):<15}', end='')
  print()
print('=-=' * 20)
while True:
  buscar = int(input('Exibir dados de qual jogador? [999] para parar: '))
  if buscar == 999: break
  if buscar >= len(lista_fut):
    print(f'Erro! Não existe jogador com código {buscar}! ')
  else:
    print(f' -- LEVANTAMENTO DO JOGADOR {lista_fut[buscar]["Nome"]}: ')
    for i, g in enumerate(lista_fut[buscar]["Gols"]):
      print(f'  no jogo {i + 1} fez {g} gols. ')
  print(f'=-=' * 20)
print('Volte Sempre! ')'''


