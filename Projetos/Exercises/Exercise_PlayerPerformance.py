dictJogadorFutebol = {}
listaAproveitamento = []
listaTime = []
while True:
    dictJogadorFutebol.clear()
    dictJogadorFutebol['Nome'] = str(input('Nome do jogador de futebol: '))
    partidasJogadas = int(input(f'Número de partidas {dictJogadorFutebol["Nome"]} jogou: '))
    listaAproveitamento.clear()
    for c in range(partidasJogadas):
        dictJogadorFutebol['Gols'] = int(input(f'Numero de gols feitos na {c + 1}ª partida: '))
    listaAproveitamento.append(dictJogadorFutebol['Gols'])
    dictJogadorFutebol['Total de gols'] = sum(listaAproveitamento)
    listaTime.append(dictJogadorFutebol.copy())
    desejaContinue = int(input('Deseja continuar?[1] Sim [2] Não: '))
    if desejaContinue == 2: break
print('Cod ', end='')
for i in dictJogadorFutebol.keys():
    print(f'{i:<15} ', end='')
print()
for key, value in enumerate(listaTime):
    print(f'{key:>4} ', end='')
    for d in value.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    buscarJogador = int(input('Deseja mostrar os dados de qual jogador? (999 para sair): '))
    if buscarJogador == 999: break
    if buscarJogador >= len(listaTime):
        print(f'Não existe nenhum jogador com este código: {buscarJogador}')
    else:
        print(f'{listaTime[buscarJogador]["Nome"]}')
        for h, g in enumerate(listaTime[buscarJogador]['Gols']):
            print(f'No no jogo {h + 1} fez {g} gols.')
    print()
print()