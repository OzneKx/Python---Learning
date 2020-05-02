listData = []
dictData = {}
totalMulheres = somaIdade = 0
while True:
    dictData['Nome'] = str(input('Informe seu nome: ')).strip().title()
    dictData['Sexo'] = str(input('Informe seu sexo: ')).strip().upper()[0]
    while dictData['Sexo'] not in 'MF':
        dictData['Sexo'] = str(input('Informe seu sexo corretamente: ')).strip().upper()[0]
    if dictData['Sexo'] == 'F':
        totalMulheres += 1
    dictData['Idade'] = int(input('Informe sua idade: '))
    somaIdade += dictData['Idade']
    listData.append(dictData.copy())
    desejaContinuarIsso = int(input('Deseja continuar?[1] Sim e [2] Não: '))
    if desejaContinuarIsso == 2: break
mediaIdadeGrupo = (somaIdade) / (len(listData))
print()
print(f'A) Foram cadastradas {len(listData)} pessoas. ')
print(f'B) A média de idade do grupo foi de {mediaIdadeGrupo:.2f}')
print(f'C) O total de mulheres cadastradas foi: {totalMulheres}')
print(f'D) Pessoas com idade acima da média:')
for pessoas in listData:
    if pessoas['Idade'] > mediaIdadeGrupo:
        for key, value in pessoas.items():
            print(f'{key} = {value}; ', end='')
    elif pessoas['Idade'] == mediaIdadeGrupo:
        print('Apenas uma pessoa foi cadastrada! ')