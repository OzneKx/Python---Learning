dictEstado = {}
listaBrasilEstado = []
for c in range(1, 3 + 1, 1):
    dictEstado['UF'] = str(input('Unidade Federativa: '))
    dictEstado['sigla'] = str(input('Sigla do estado: '))
    listaBrasilEstado.append(dictEstado.copy())
#print(listaBrasilEstado)
for estado in listaBrasilEstado:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')