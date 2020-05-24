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


dict_pessoas = {}
lista_pessoas = []
while True:
  dict_pessoas["Nome"] = str(input('Seu nome: '))
  dict_pessoas["Sexo"] = str(input('Seu Sexo: [M/F]: ')).strip().upper()[0]
  if dict_pessoas["Sexo"] == "F":
    lista_pessoas.append(dict_pessoas["Sexo"])
  dict_pessoas["Idade"] = int(input('Sua idade: '))
  continuar = int(input('Deseja continuar? [1] Sim [2] Não:'))
  if continuar == 2: break
media_idade = sum(dict_pessoas["Idade"]) / len(dict_pessoas)
print(f'Foram cadastradas {len(dict_pessoas)} pessoas.')
print(f'A média de idade do grupo é igual a {media_idade}')
print(f'Lista de mulheres: {lista_pessoas}')
for c in dict_pessoas["Idade"]:
  if c > media_idade:
    lista_pessoas.clear()
    lista_pessoas.append(c)
print(f'Pessoas com idade superior a média: {lista_pessoas}')
