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


from datetime import date
ano_atual = date.today().year
dict_cadastro = {"Nome": 0 ,
                 "Carteira de Trabalho": 0, 
                 "Ano de Contratação": 0, "Salário": 0
                 }
for k in dict_cadastro.keys():
  dict_cadastro[k] = input(f'Digite seu {k}: ')
  nascimento = int(input('Ano de nascimento: '))
  dict_cadastro["Idade"] = (ano_atual - nascimento)
  dict_cadastro["Anos restantes de Trabalho"] = ((ano_atual - dict_cadastro["Ano de Contratação"]) +  dict_cadastro["Idade"])
  if dict_cadastro["Anos restantes de Trabalho"] > 35:
    print(f'Você já está aposentado! ')
  else:
    print(f'Ainda faltam {((ano_atual - dict_cadastro["Ano de Contratação"]) +  dict_cadastro["Idade"])} anos para se aposentar. ')
for k, v in dict_cadastro.items():
  print(f'{k} tem valor igual a = {v}')
