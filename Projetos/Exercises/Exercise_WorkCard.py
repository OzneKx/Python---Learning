from datetime import date
anoAtual = date.today().year
dictCTPS = {}
dictCTPS['Nome'] = str(input('Seu nome: '))
anoNascimento = int(input('Ano de nascimento: '))
dictCTPS['Idade'] = (anoAtual - anoNascimento)
dictCTPS['Carteira de Trabalho'] = int(input('Carteira de trabalho (digite 0 caso não tenha): '))
if dictCTPS['Carteira de Trabalho'] == 0:
    for key, value in dictCTPS.items():
        print(f'{key} tem o valor {value}')
else:
    dictCTPS['Ano de Contratação'] = int(input('Ano de sua contratação: '))
    dictCTPS['Salário'] = float(input('Seu salário: R$'))
    dictCTPS['Aposentadoria'] = dictCTPS['Idade'] + ((dictCTPS['Ano de Contratação'] + 35) - anoAtual)
for key, value in dictCTPS.items():
    print(f'{key} tem o valor {value}')