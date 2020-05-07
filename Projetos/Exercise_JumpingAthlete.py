nomeAtleta = True
atleta = 1
listaSaltos = []
while nomeAtleta:
    nomeAtleta = str(input('Digite o nome do atleta: '))
    if nomeAtleta == '':
        break
    else:
        salto = 1
        for c in range(1, 5 + 1, 1):
            distanciaSalto = float(input('Distancia do {}º salto: '.format(c)))
            listaSaltos.append(distanciaSalto)
            salto += 1
        print('Atleta: {}'.format(nomeAtleta))
        salto = 1
        count = 0
        for c in range(1, 5 + 1, 1):
            print('{}° salto: {} m'.format(salto, listaSaltos[count]))
            salto += 1
            count += 1
        print('Melhor salto: {} m'.format(max(listaSaltos)))
        print('Pior salto: {} m'.format(min(listaSaltos)))
        listaSaltos.remove(max(listaSaltos))
        listaSaltos.remove(min(listaSaltos))
        mediaSaltos = sum(listaSaltos) / len(listaSaltos)
        print('Média dos outros saltos: {} m'.format(round(mediaSaltos, 2)))
        print('Resultado Final: {}: {} m'.format(nomeAtleta, round(mediaSaltos, 2)))
        atleta += 1